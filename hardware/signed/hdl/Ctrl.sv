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
   input logic op,
   input logic abs,
   output logic new_s,
   output logic mult,
   output logic CAU_w_en,
   output logic 
   output logic sel[N-1:0], // Select 
   output logic acc_sel[2**N:0] // Checar
);

   State current_s, next_s;
   reg count_row[N-1:0];
   reg count_acc[$clog2(N)-1:0];
   reg CAU_acc_sel[2**N:0]

   always_ff @( posedge clk or rst ) begin
      if (rst) begin
        current_s <= s_rst;
      end
      else begin
        current_s <= next_s;
      end

   end
   always_comb begin
      mult = 1'b0; 
      case (current_s)
         s_rst:
            next_s = idle;
         idle:
            if (op == 1'b1) begin
               if (abs == 1'b1) begin
                  next_s = abs;
               end
                  next_s = mul;
            end
         add:

         mul:
            mult = 1'b1;
         acc:
         abs:
         default: 
            next_s = idle;
      endcase
      
   end
    
endmodule