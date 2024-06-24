typedef enum  { 
   s_rst,
   idle,
   add,
   mul,
   acc,
   abs
} State;

module Ctrl #(
   parameter integer N =1 
) (
   input logic clk, rst,
   output logic sel[N-1:0]
);

   State current_s, next_s;

   always_ff @( posedge clk or rst ) begin
      if (rst) begin
        current_s <= s_rst;
      end
      else begin
        current_s <= next_s;
      end

   end
   always_comb begin 
      case (current_s)
         s_rst: 
         default: 
      endcase
      
   end
    
endmodule