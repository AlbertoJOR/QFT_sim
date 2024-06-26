module mul_mux #(
    parameter N = 2,
    parameter DATA_W = 32
)(
    input logic [DATA_W*N-1 :0 ] A,
    input logic [$clog2(N)-1: 0] sel,
    output logic [DATA_W-1: 0] S
);
    reg [DATA_W -1 :0] A_aux [N-1:0];

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin
            always_comb begin 
                A_aux[i] = A[i*DATA_W +: DATA_W];  // Assign each 8-bit chunk to the corresponding byte
            end
        end
    endgenerate


    if(N == 1) begin
        assign S = A_aux[0];
    end else begin
        assign S = A_aux[sel];
    end

endmodule