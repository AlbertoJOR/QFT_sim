`timescale 1ns/1ps
module Q1CAU #(
    parameter integer DATA_W = 32
)(
    input logic clk,
    input logic rst,
    input logic [DATA_W -1 : 0] A_r [1:0],
    input logic [DATA_W -1 : 0] A_i [1:0],
    input logic [DATA_W -1 : 0] B_r [1:0],
    input logic [DATA_W -1 : 0] B_i [1:0],
    input logic sum,
    input logic abs,
    input logic sel,
    input logic w_en,


    output logic overflow,
    output logic [DATA_W -1 : 0] S_r [1:0],
    output logic [DATA_W -1 : 0] S_i [1:0]

);
    wire [DATA_W *2 -1: 0] S_ma, S_mb, S_mc;
    wire [DATA_W * 2-1 : 0] A_ma [1 : 0];
    wire [DATA_W * 2-1 : 0] A_mb [1 : 0];
    wire [DATA_W * 2-1 : 0] A_mc [1 : 0];

    wire [DATA_W *2 -1:0] reg0_i, reg0_o, reg1_i, reg1_o;
    wire [1:0] over;

    register_m #(.DATA_W (DATA_W*2)) reg0(
        .clk(clk),
        .rst(rst),
        .w_en(w_en),
        .A(reg0_i),
        .S(reg0_o)
    );

    register_m #(.DATA_W (DATA_W*2)) reg1(
        .clk(clk),
        .rst(rst),
        .w_en(w_en),
        .A(reg1_i),
        .S(reg1_o)
    );
    assign A_ma[0] = {A_r[0], A_i[0]};
    assign A_ma[1] = reg0_o;

    nmux #(.DATA_W(2*DATA_W), .N(2)) muxa(
        .A(A_ma),
        .S(S_ma),
        .sel(sel)
    );

    assign A_mb[0] = {B_r[0], B_i[0]};
    assign A_mb[1] = reg1_o;

    nmux #(.DATA_W(2*DATA_W), .N(2)) muxb(
        .A(A_mb),
        .S(S_mb),
        .sel(sel)
    );

    assign A_mc[0] = {A_r[1], A_i[1]};
    assign A_mc[1] = reg1_o;

    nmux #(.DATA_W(2*DATA_W), .N(2)) muxc(
        .A(A_mc),
        .S(S_mc),
        .sel(sel)
    );

    CAU #(.DATA_W(DATA_W)) cau1(
        .A_r(S_ma[DATA_W*2-1:DATA_W]),
        .A_i(S_ma[DATA_W-1:0]),
        .B_r(S_mb[DATA_W*2-1:DATA_W]),
        .B_i(S_mb[DATA_W-1:0]),
        .sum(sum),
        .abs(abs),
        .S_r(reg0_i[DATA_W*2-1:DATA_W]),
        .S_i(reg0_i[DATA_W-1:0]),
        .overflow(over[0])
    );


    CAU #(.DATA_W(DATA_W)) cau2(
        .A_r(S_mc[DATA_W*2-1:DATA_W]),
        .A_i(S_mc[DATA_W-1:0]),
        .B_r(B_r[1]),
        .B_i(B_i[1]),
        .sum(sum),
        .abs(abs),
        .S_r(reg1_i[DATA_W*2-1:DATA_W]),
        .S_i(reg1_i[DATA_W-1:0]),
        .overflow(over[1])
    );
    assign overflow =| over;
    assign S_r[0] = reg0_o[DATA_W*2-1:DATA_W];
    assign S_i[0] = reg0_o[DATA_W-1:0];
    assign S_r[1] = reg1_o[DATA_W*2-1:DATA_W];
    assign S_i[1] = reg1_o[DATA_W-1:0];

endmodule