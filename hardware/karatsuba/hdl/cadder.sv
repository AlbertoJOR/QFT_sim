module cadder #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 :0] A_real,
    input logic [DATA_W - 1 :0] A_img,
    input logic [DATA_W - 1 :0] B_real,
    input logic [DATA_W - 1 :0] B_img,
    output logic [DATA_W - 1: 0] S_real,
    output logic [DATA_W - 1: 0] S_img
);
    wire [DATA_W : 0] r_real, r_img;
    assign r_real = A_real + B_real;
    assign r_img = A_img + B_img;

    // Revisa si se elimina el bit más significativo
    assign S_img = r_img[DATA_W - 1: 0];
    assign S_real = r_real[DATA_W - 1: 0];
    
endmodule