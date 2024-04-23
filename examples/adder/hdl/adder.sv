`timescale 1ns/1ps

module adder #(
    parameter integer DATA_W = 4
)(
    input logic unsigned[DATA_W -1 :0] A,
    input logic unsigned[DATA_W -1 :0] B,
    output logic unsigned[DATA_W  :0] X
);
    assign X = A + B;


    // Dump waves
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(1, adder);
    end

endmodule