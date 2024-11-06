`timescale 1ns/1ps
module VCMAC #(
    parameter integer DATA_W = 32,
    parameter integer N = 2
)(
    input logic clk, rst,
    input logic [DATA_W -1 : 0] A_r[N-1:0],
    input logic [DATA_W -1 : 0] A_i[N-1:0],
    input logic [DATA_W -1 : 0] B_r[N-1:0],
    input logic [DATA_W -1 : 0] B_i[N-1:0],
    input logic acc,
    input logic abs,
    input logic w_en,
    input logic mult,


    output logic overflow,
    output logic [DATA_W -1 : 0] S_r[N-1:0],
    output logic [DATA_W -1 : 0] S_i[N-1:0]  

);
    wire acc_en, mult_en;
    wire [N-1:0] over;
    assign acc_en = w_en & acc & ~mult;
    assign mult_en = w_en & mult & ~acc;
    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : CMAC_gen
            CMAC #(.DATA_W(DATA_W)) cmac_ (
                .clk(clk),
                .rst(rst),
                .A_r(A_r[i]),
                .A_i(A_i[i]),
                .B_r(B_r[i]),
                .B_i(B_i[i]),
                .acc(acc),
                .abs(abs),
                .acc_en(acc_en),
                .mult_en(mult_en),
                .overflow(over[i]),
                .S_r(S_r[i]),
                .S_i(S_i[i])
            );
        end
    endgenerate;
    assign overflow = |over;
endmodule