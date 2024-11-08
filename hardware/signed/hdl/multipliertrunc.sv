`timescale 1ns/1ps

module multipliertrunc #(
    parameter integer DATA_W = 16
)
(
    input logic [DATA_W -1 : 0] A,
    input logic [DATA_W -1 : 0] B,
    output logic [DATA_W  -1 :0] S
);  
    wire [DATA_W*2-1:0] aux;
    assign aux = A* B;
    assign S = aux[DATA_W-1:0];
endmodule