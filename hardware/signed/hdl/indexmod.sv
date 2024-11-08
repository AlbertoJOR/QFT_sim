`timescale 1ns/1ps
module indexmod #(
    parameter integer N = 2,
    parameter integer WIDTH = $clog2(N)
)(
    input logic   [WIDTH-1:0] A,
    output logic  [WIDTH-1:0] S [N-1:0]

);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : mult_gen
            //multiplierkaratrunc #(.DATA_W(WIDTH)) mult_ (
            multipliertrunc #(.DATA_W(WIDTH)) mult_ (
                .A(A),         
                .B(i),         
                .S(S[i])       
            );
        end
    endgenerate

endmodule