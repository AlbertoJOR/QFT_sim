`timescale 1ns/1ps

module adder #(
    parameter integer DATA_W = 32
)(
    input logic [DATA_W -1 :0] A,
    input logic [DATA_W -1 :0] B,
    input logic  Carry,
    output logic [DATA_W  :0] S
);
    assign S = A + B + { {DATA_W-1{1'b0}},Carry};
endmodule