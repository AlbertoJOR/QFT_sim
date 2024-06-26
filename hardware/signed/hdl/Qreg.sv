module Qreg #(
    parameter integer N = 1,
    parameter integer DATA_W = 32
) (
    input logic clk,
    input logic rst,
    input logic w_en,
    input logic  [((2 ** N) *DATA_W*2)- 1:0] A,
    output logic  [((2 ** N) *DATA_W*2)- 1:0] S
);
 

    genvar  i;

    generate
        for (i = 0; i < 2**N ; i = i + 1) begin

            register_m #(.DATA_W (DATA_W*2)) reg_(
                .clk(clk),
                .rst(rst),
                .w_en(w_en),
                .A(A[i*DATA_W*2  +: (DATA_W*2)]),
                .S(S[i*DATA_W*2  +: (DATA_W*2)])
            );
            
        end
        
    endgenerate
    
endmodule