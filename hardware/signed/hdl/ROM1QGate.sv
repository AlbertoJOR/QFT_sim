module ROM1QGate #(
    parameter DATA_W = 32,            
    parameter [DATA_W-1:0] D0r = 32'h00000000, 
    parameter [DATA_W-1:0] D0i = 32'h00000000, 
    parameter [DATA_W-1:0] D1r = 32'h00000000, 
    parameter [DATA_W-1:0] D1i = 32'h00000000, 
    parameter [DATA_W-1:0] D2r = 32'h00000000, 
    parameter [DATA_W-1:0] D2i = 32'h00000000, 
    parameter [DATA_W-1:0] D3r = 32'h00000000, 
    parameter [DATA_W-1:0] D3i = 32'h00000000
)(
    input logic addr,
    output logic [DATA_W*4-1:0] gate_row
);

    always @* begin
        case (addr)
            1'b0: gate_row = {D0r, D0i, D1r, D1i};
            1'b1: gate_row = {D2r, D2i, D3r, D3i};
            default: gate_row = {(DATA_W*4){1'b0}}; 
        endcase
    end

endmodule
