module Multiplier8x8(
    input [7:0] multiplicand,
    input [7:0] multiplier,
    input clk,
    output reg [15:0] product
);

reg [15:0] accumulator;
integer i;
wire [15:0] extended_multiplicand;
assign extended_multiplicand = {8'b0, multiplicand};

always @(posedge clk) begin
    accumulator <= 0; // Clear accumulator on every clock cycle
    for (i = 0; i < 8; i = i + 1) begin
        if (multiplier[i] == 1) begin
            accumulator <= accumulator + ( extended_multiplicand << i);
        end
    end
end

assign product = accumulator;

endmodule
