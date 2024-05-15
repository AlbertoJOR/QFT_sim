`timescale 1ns/1ps
module multiplierkara #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 : 0] A,
    input logic [DATA_W - 1 : 0] B,
    output logic [DATA_W * 2 - 1 : 0] S
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

    wire [DATA_W: 0] m1inv, m2inv;
    
    inverter #(.DATA_W(DATA_W+1)) inv1(
        .A({1'b0,m1}),
        .S(m1inv)
    );
    
    inverter #(.DATA_W(DATA_W+1)) inv2(
        .A({1'b0,m2}),
        .S(m2inv)
    );

    wire [DATA_W+1: 0] invsum;

    subs #(.DATA_W(DATA_W+1)) invm1m2(
        .A(m1inv),
        .B(m2inv),
        .Carry(1'b0),
        .S(invsum)
    );

    wire [DATA_W+2:0] invsumext;
    wire [DATA_W+3:0] m3subs;

    signextend #(.DATA_W(DATA_W+2), .EXT_W(1)) ext1(
        .A(invsum),
        .S(invsumext)
    );

    subs2 #(.DATA_W(DATA_W+3)) m3adder(
        .A(invsumext),
        .B({1'b0,m3}),
        .Carry(1'b0),
        .S(m3subs)
    );

    wire [DATA_W + 4 + DATA_W/2 -1:0] m3subspad;

    padderright #(.DATA_W(DATA_W+4), .EXT_W(DATA_W/2)) padder
    (
        .A(m3subs),
        .S(m3subspad)
    );
    wire [DATA_W*2-1:0] m1extend, m2extend, m3extend;

    signextend #(.DATA_W(DATA_W + 4 + DATA_W/2), .EXT_W(DATA_W/2 -4)) extm3(
        .A(m3subspad),
        .S(m3extend)
    );

    padderleft #(.DATA_W(DATA_W), .EXT_W(DATA_W)) extm2(
        .A(m2),
        .S(m2extend)
    );

    padderright #(.DATA_W(DATA_W), .EXT_W(DATA_W)) extm1(
        .A(m1),
        .S(m1extend)
    );

    wire [DATA_W*2:0] summ1, summ2;

    adder #(.DATA_W(DATA_W*2)) adderext1(
        .A(m1extend),
        .B(m2extend),
        .Carry(1'b0),
        .S(summ1)
    );

    adder #(.DATA_W(DATA_W*2)) adderext2(
        .A(summ1[DATA_W*2-1:0]),
        .B(m3extend),
        .Carry(1'b0),
        .S(summ2)
    );

    assign S = summ2[DATA_W *2-1:0];

endmodule