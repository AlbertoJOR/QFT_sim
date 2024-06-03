`timescale 1ns/1ps

module multiplier #(
    parameter integer DATA_W = 16
)
(
    input logic [DATA_W -1 : 0] A,
    input logic [DATA_W -1 : 0] B,
    output logic [DATA_W * 2 -1 :0] S
);
    assign S = A * B;
endmodule