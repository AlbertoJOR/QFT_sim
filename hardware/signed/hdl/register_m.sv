module register_m#(
    parameter integer DATA_W = 32
)
(
    input clk,
    input rst,
    input w_en,
    input logic [DATA_W - 1 :0] A,
    output logic [DATA_W - 1 : 0] S
);

    reg [DATA_W -1: 0] Q;

    initial begin
        Q = {DATA_W{1'b0}};
    end

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            Q <= {DATA_W{1'b0}};

        end 
        else begin
            if (w_en) begin
                Q <= A;
            end
        end
    end
    assign S = Q;

endmodule;