`timescale 1ns/1ps
module register_m #(
    parameter integer DATA_W = 32
) (
    input logic clk,
    input logic rst,
    input logic w_en,
    input logic [DATA_W - 1 : 0] A,
    output logic [DATA_W - 1 : 0] S
);

    // Bloque secuencial sensible al flanco positivo de clk o rst
    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            S <= {DATA_W{1'b0}};  // Reiniciar el registro
        end 
        else if (w_en) begin
            S <= A;               // Actualizar S con A si w_en está activo
        end
    end

endmodule