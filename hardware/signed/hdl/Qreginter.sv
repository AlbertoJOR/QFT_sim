module Qreginter #(
    parameter integer N = 1,
    parameter integer DATA_W = 32
) (
    input logic clk,
    input logic rst,
    input logic w_en,
    input logic all,
    input logic [N-1:0] sel,
    input logic  [((2 ** N) *DATA_W*2)- 1:0] A,
    output logic  [((2 ** N) *DATA_W*2)- 1:0] S
);
    wire [2**N-1 :0] w_en_out_aux;

    n_w_en #(.N(N))n_sel(
        .sel(sel),
        .all(all),
        .w_en(w_en),
        .w_en_out(w_en_out_aux)
    );

    genvar  i;
    generate
        for (i = 0; i < 2**N ; i = i + 1) begin:block_reg

            register_m #(.DATA_W (DATA_W*2)) R(
                .clk(clk),
                .rst(rst),
                .w_en(w_en_out_aux[i]),
                .A(A[(2**N-i-1)*DATA_W*2  +: (DATA_W*2)]),
                .S(S[(2**N-i-1)*DATA_W*2  +: (DATA_W*2)])
            );
            
        end
        
    endgenerate
    
endmodule