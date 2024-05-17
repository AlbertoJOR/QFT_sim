`timescale 1ns/1ps
module cmultiplier #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 :0] A_real,
    input logic [DATA_W - 1 :0] A_img,
    input logic [DATA_W - 1 :0] B_real,
    input logic [DATA_W - 1 :0] B_img,
    output logic [DATA_W * 2 - 1: 0] S_real,
    output logic [DATA_W * 2 - 1: 0] S_img
    // output logic [DATA_W * 2: 0] S_real,
    // output logic [DATA_W * 2: 0] S_img
);
    wire [DATA_W * 2 - 1 :0] real_part, img_part, ArBi, BrAi, img_part_inv;

    multiplierkara #(.DATA_W(DATA_W)) mult1 (
        .A(A_real),
        .B(B_real),
        .S(real_part)
    );

    multiplierkara #(.DATA_W(DATA_W)) mult2 (
        .A(A_real),
        .B(B_img),
        .S(ArBi)
    );

    multiplierkara #(.DATA_W(DATA_W)) mult3 (
        .A(B_real),
        .B(A_img),
        .S(BrAi)
    );

    multiplierkara #(.DATA_W(DATA_W)) mult4 (
        .A(A_img),
        .B(B_img),
        .S(img_part)
    );

    inverter #(.DATA_W(DATA_W * 2)) inv(
        .A(img_part),
        .S(img_part_inv)
    );

    wire [DATA_W * 2  :0] res_real, res_img;

    adder #(.DATA_W(DATA_W * 2)) addreal(
        .A(real_part),
        .B(img_part_inv),
        .Carry(1'b0),
        .S(res_real)
    );

    adder #(.DATA_W(DATA_W * 2)) addimg(
        .A(ArBi),
        .B(BrAi),
        .Carry(1'b0),
        .S(res_img)
    );

    assign S_real = res_real[DATA_W * 2 - 1: 0];
    assign S_img = res_img[DATA_W * 2 - 1: 0];
    // Revisa si es necesario eliminar ese bit.
    // assign S_real = res_real[DATA_W * 2: 0];
    // assign S_img = res_img[DATA_W * 2: 0];

    

    
endmodule