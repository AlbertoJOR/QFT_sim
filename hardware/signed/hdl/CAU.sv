`timescale 1ns/1ps
module CAU #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W -1 :0 ] A_r,
    input logic [DATA_W -1 :0 ] A_i,
    input logic [DATA_W -1 :0 ] B_r,
    input logic [DATA_W -1 :0 ] B_i,
    input logic sum,
    input logic abs,

    output logic [DATA_W -1 : 0 ] S_r,
    output logic [DATA_W -1 : 0 ] S_i,
    output logic overflow


);


    wire [1 : 0] over;
    wire [DATA_W -1:0] S_r_s [1 : 0];
    wire [DATA_W -1:0] S_i_s [1 : 0];
    wire [DATA_W -1 :0] A_ic;

    assign A_ic = {~A_i[DATA_W-1],A_i[DATA_W-2:0]};
    

    ckarasign #(.DATA_W(DATA_W)) mult (
        .A_real(A_r),
        .A_img(A_i),
        .B_real(abs? A_r : B_r),
        .B_img(abs? A_ic : B_i),
        .S_real(S_r_s[0]),
        .S_img(S_i_s[0]),
        .overflow(over[0])
    );
    

    caddersign #(.DATA_W(DATA_W)) addr(
        .A_real(A_r),
        .A_img(A_i),
        .B_real(B_r),
        .B_img(B_i),
        .S_real(S_r_s[1]),
        .S_img(S_i_s[1]),
        .overflow(over[1])
    );


    assign overflow =| over;

    assign S_r = sum ? S_r_s[1] : S_r_s[0];
    assign S_i = sum ? S_i_s[1] : S_i_s[0];





endmodule;
