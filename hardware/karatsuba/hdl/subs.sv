`timescale 1ns/1ps

module subs #(
    parameter integer DATA_W = 32
)(
    input logic [DATA_W -1 :0] A,
    input logic [DATA_W -1 :0] B,
    input logic  Carry,
    output logic [DATA_W  :0] S
);
    wire [DATA_W :0] res;
    assign res = A + B + { {DATA_W-1{1'b0}},Carry};
    assign S = {res[DATA_W]|res[DATA_W-1],res[DATA_W-1:0]};
endmodule