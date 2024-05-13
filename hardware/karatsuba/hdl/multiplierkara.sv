`timescale 1ns/1ps
module multiplierkara #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 : 0] A,
    input logic [DATA_W - 1 : 0] B,
    input logic [DATA_W * 2 - 1 : 0] S
);
    // P1 = Ahigh * Bhigh;
    // P2 = Alow * Blow;
    // P3 = (Ahigh + Alow) * (Bhigh + Blow) - P1 - P2;

    wire [DATA_W/2 - 1:0] A_h, A_l, B_h, B_l;
    wire [DATA_W - 1:0] m1, m2;
    assign A_h = A[DATA_W - 1 : DATA_W/2];
    assign B_h = B[DATA_W - 1 : DATA_W/2];
    assign A_l = A[DATA_W/2 - 1 : 0];
    assign B_l = B[DATA_W/2 - 1 : 0];

    multiplier #(.DATA_W(DATA_W/2)) mult1 (
        .A(A_h),
        .B(B_h),
        .S(m1)
    );

    multiplier #(.DATA_W(DATA_W/2)) mult2 (
        .A(A_l),
        .B(B_l),
        .S(m2)
    );

    wire [DATA_W/2 :0] sA, sB;

    adder #(.DATA_W(DATA_W/2)) adderA(
        .A(A_h),
        .B(A_l),
        .Carry(1'b0),
        .S(sA)
    );

    adder #(.DATA_W(DATA_W/2)) adderB(
        .A(B_h),
        .B(B_l),
        .Carry(1'b0),
        .S(sB)
    );
    
    wire [DATA_W+1 : 0] m3;

    multiplier #(.DATA_W(DATA_W/2 + 1)) mult3 (
        .A(sA),
        .B(sB),
        .S(m3)
    );

    wire [DATA_W-1: 0] im1, im2;

    inverter #(.DATA_W(DATA_W)) inv1(
        .A(m1),
        .S(im1)
    );

    inverter #(.DATA_W(DATA_W)) inv2(
        .A(m1),
        .S(im1)
    );

    wire [DATA_W: 0] sinv;

    adder #(.DATA_W(DATA_W)) invsum(
        .A(im1),
        .B(im2),
        .Carry(1'b0),
        .S(sinv)
    );





endmodule