`timescale 1ns/1ps
module VMux #(
    parameter integer N = 2,
    parameter integer DATA_W = 32,
    parameter integer SEL_W = $clog2(N)
)(
    input logic [SEL_W -1 : 0] SEL [N-1:0],
    input logic [DATA_W*2-1: 0] A [N-1:0],
    output logic [DATA_W*2-1: 0] S [N-1:0]
);
    genvar  i;
    generate
       for (i = 0 ; i < N ; i = i + 1) begin: sel_gen
            nmux #(.N(N), .DATA_W(DATA_W*2)) mux_(
                .A(A),
                .S(S[i]),
                .sel(SEL[i])
            );
       end 
    endgenerate

endmodule 