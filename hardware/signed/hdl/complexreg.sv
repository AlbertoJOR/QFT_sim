module complexreg#(
    parameter integer DATA_W = 32
)
(
    input clk,
    input rst,
    input w_en,
    input logic [DATA_W - 1 :0] A_r,
    input logic [DATA_W - 1 :0] A_i,
    output logic [DATA_W - 1 : 0] S_r,
    output logic [DATA_W - 1 : 0] S_i
);

    reg [DATA_W -1: 0] Q_i, Q_r;

    initial begin
        Q_r = {DATA_W{1'b0}};
        Q_i = {DATA_W{1'b0}};
    end

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            Q_r <= {DATA_W{1'b0}};
            Q_i <= {DATA_W{1'b0}};

        end 
        else begin
            if (w_en) begin
                Q_r <= A_r;
                Q_i <= A_i;
            end
        end
    end
    assign S_r = Q_r;
    assign S_i = Q_i;

endmodule;