`timescale  1ns/1ps
module padderleft #(
    parameter integer DATA_W = 32,
    parameter integer EXT_W = 1
)(
    input logic [DATA_W -1 : 0] A,
    output logic [DATA_W + EXT_W - 1: 0] S
);
    assign S = {{EXT_W{1'b0}},A};

endmodule 