module n_w_en #(
    parameter integer N = 1
)
(
    input logic [N-1:0] sel,
    input logic all,
    input logic w_en,
    output logic [(2**N)-1:0] w_en_out
);
    always_comb begin
        w_en_out = {(2**N){1'b0}};

        if(w_en == 1'b1) begin
            if(all == 1'b1) begin
                w_en_out = {(2**N){1'b1}};
            end else begin
                w_en_out[sel] = 1'b1;
            end
        end
    end
endmodule