module register_d #(
    parameter integer DATA_W = 32
) (
    input logic clk,
    input logic rst,
    input logic w_en,
    input logic [DATA_W - 1 : 0] A,
    output logic [DATA_W - 1 : 0] S
);

    logic [DATA_W - 1 : 0] A_delayed;  // Registro intermedio para retraso

    // Bloque secuencial para registrar el valor de A y actualizar S
    always_ff @(posedge clk or posedge rst) begin
        S <= A_delayed;   // S toma el valor de A_delayed en el siguiente ciclo
        if (rst) begin
            S <= {DATA_W{1'b0}};
            A_delayed <= {DATA_W{1'b0}};
        end 
        else if (w_en) begin
            A_delayed <= A;   // Captura A en el primer ciclo
        end
    end

endmodule