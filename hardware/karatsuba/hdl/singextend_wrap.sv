`timescale 1ns/1ps
module singextend_wrap #(
    parameter integer DATA_W = 8,
    parameter integer EXT_W = 4
)(
    input logic [DATA_W - 1 : 0] A, 
    output logic [DATA_W + EXT_W - 1: 0] S
);

        singextend #(.DATA_W(DATA_W), .EXT_W(EXT_W)) signext (
        .A(A),
        .S(S)
    );

endmodule