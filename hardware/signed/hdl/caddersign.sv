`timescale 1ns/1ps
module caddersign #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 :0] A_real,
    input logic [DATA_W - 1 :0] A_img,
    input logic [DATA_W - 1 :0] B_real,
    input logic [DATA_W - 1 :0] B_img,
    output logic [DATA_W - 1: 0] S_real,
    output logic [DATA_W - 1: 0] S_img,
    output logic overflow
);
    wire overR, overI;
    addersign #(.DATA_W(DATA_W)) addR(
        .A(A_real),
        .B(B_real),
        .S(S_real),
        .overflow(overR)
    );

    addersign #(.DATA_W(DATA_W)) addI(
        .A(A_img),
        .B(B_img),
        .S(S_img),
        .overflow(overI)
    );   

    assign overflow = overI | overR;
    
endmodule