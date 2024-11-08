`timescale 1ns/1ps
module CMAC2 # (
    parameter integer DATA_W = 32
)(
    input logic clk, rst,
    input logic [DATA_W*2 -1 : 0] A,
    input logic [DATA_W*2 -1 : 0] B,
    input logic acc,
    input logic abs,
    input logic acc_en,
    input logic mult_en,


    output logic overflow,
    output logic [DATA_W*2 -1 : 0] S
);
    
    wire [DATA_W *2 -1:0] reg_acc, reg_mult, mux_acc_S, mux_mult_S;
    wire [DATA_W-1:0] S_i_res, S_r_res;
    wire [DATA_W * 2-1 : 0] mux_acc_A [1 : 0];
    wire [DATA_W * 2-1 : 0] mux_mult_A [1 : 0];

    assign mux_mult_A[0] = A;
    assign mux_acc_A[0] = B;

    register_m #(.DATA_W(DATA_W*2)) accu_reg(
        .clk(clk),
        .rst(rst),
        .w_en(acc_en),
        .A({S_r_res, S_i_res}),
        .S(reg_acc)
    );

    register_m #(.DATA_W(DATA_W*2)) mult_reg(
        .clk(clk),
        .rst(rst),
        .w_en(mult_en),
        .A({S_r_res, S_i_res}),
        .S(reg_mult)
    );



    assign mux_mult_A[1] = reg_mult;
    assign mux_acc_A[1] = reg_acc;

    nmux #(.DATA_W(2*DATA_W), .N(2)) mux_acc(
        .A(mux_acc_A),
        .S(mux_acc_S),
        .sel(acc)
    );
    
    nmux #(.DATA_W(2*DATA_W), .N(2)) mux_mult(
        .A(mux_mult_A),
        .S(mux_mult_S),
        .sel(acc)
    );

    CAU #(.DATA_W(DATA_W)) cau(
        .A_r(mux_mult_S[DATA_W*2-1:DATA_W]),
        .A_i(mux_mult_S[DATA_W-1:0]),
        .B_r(mux_acc_S[DATA_W*2-1:DATA_W]),
        .B_i(mux_acc_S[DATA_W-1:0]),
        .sum(acc),
        .abs(abs),
        .S_r(S_r_res),
        .S_i(S_i_res),
        .overflow(overflow)
    );
    assign S = {S_r_res, S_i_res};
    
    
endmodule