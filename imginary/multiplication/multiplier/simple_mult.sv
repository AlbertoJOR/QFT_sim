module Multiplier(
    input [3:0] multiplicand,
    input [3:0] multiplier,
    output reg [7:0] product
);

reg [7:0] accumulator;

always @(posedge clk) begin
    accumulator <= 0; // Clear accumulator on every clock cycle
    for (i = 0; i < 4; i = i + 1) begin
        if (multiplier[i] == 1) begin
            accumulator <= accumulator + (multiplicand << i);
        end
    end
end

assign product = accumulator;

endmodule
