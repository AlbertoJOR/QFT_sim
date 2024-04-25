`timescale 1ns/1ps

module adder_doble (
    input logic unsigned[7 :0] A,
    input logic unsigned[7: 0] B, 
    output logic unsigned[8: 0] X
);
    wire [4 :0] X1_o;
    wire [4 :0] X2_o;

    adder #(.DATA_W(4)) adder_1 (
        .A(A[3:0]),
        .B(B[3:0]),
        .Carry(1'b0),
        .X(X1_o)
    );
    adder #(.DATA_W(4)) adder_2 (
        .A(A[7:4]),
        .B(B[7:4]),
        .Carry(X1_o[4]),
        .X(X2_o)
    );

    assign X = {X2_o, X1_o[3:0]};
endmodule