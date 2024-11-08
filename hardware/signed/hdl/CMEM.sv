`timescale 1ns/1ps
module CMEM #(
    parameter integer N = 2,
    parameter integer DATA_W = 32
)(
    input logic [DATA_W*2 -1 : 0] A [N-1:0],
    input logic [DATA_W*2 -1 : 0] D_in,
    input logic clk,
    input logic rst,
    input logic w_en,
    input logic new_state,
    input logic [$clog2(N)-1:0]addr,

    output logic [DATA_W*2 -1 : 0] S [N-1:0],
    output logic [DATA_W*2 -1 : 0] D_out

);

    wire [DATA_W*2-1:0] reg_out [N-1:0];

    // Instanciar registros 
    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : register_gen
            register_m #(.DATA_W(DATA_W*2)) reg_(
                .clk(clk),
                .rst(rst),
                .w_en((w_en && (addr == i)) || new_state),
                .A(new_state ? A[i] : D_in),
                .S(reg_out[i])
            );
        end
    endgenerate
    assign D_out = reg_out[addr];

    generate
        for ( i = 0 ; i < N ; i = i + 1) begin: output_gen
            assign S[i] = reg_out[i];
        end
    endgenerate


endmodule