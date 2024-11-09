`timescale 1ns/1ps
module VCMAC2 #(
    parameter integer DATA_W = 32,
    parameter integer N = 2
)(
    input logic clk, rst,
    input logic [DATA_W*2 -1 : 0] A[N-1:0],
    input logic [DATA_W*2 -1 : 0] B[N-1:0],
    input logic acc,
    input logic abs,
    input logic w_en_mult,
    input logic w_en_acc,


    output logic overflow,
    output logic [DATA_W*2 -1 : 0] S[N-1:0]

);
    wire [N-1:0] over;
    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : CMAC_gen
            CMAC2 #(.DATA_W(DATA_W)) cmac_ (
                .clk(clk),
                .rst(rst),
                .A(A[i]),
                .B(B[i]),
                .acc(acc),
                .abs(abs),
                .acc_en(w_en_acc),
                .mult_en(w_en_mult),
                .overflow(over[i]),
                .S(S[i])
            );
        end
    endgenerate;
    assign overflow = |over;
endmodule