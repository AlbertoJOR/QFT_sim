module nmux #(
    parameter N = 2,
    parameter DATA_W = 32
)(
    input logic [DATA_W-1 :0 ] A [N-1: 0],
    input logic [$clog2(N)-1: 0] sel,
    output logic [DATA_W-1: 0] S
);

    if(N == 1) begin
        assign S = A[0];
    end else begin
        assign S = A[sel];
    end

endmodule