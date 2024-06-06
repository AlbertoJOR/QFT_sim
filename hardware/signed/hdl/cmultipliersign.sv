`timescale 1ns/1ps
module cmultipliersign #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 :0] A_real,
    input logic [DATA_W - 1 :0] A_img,
    input logic [DATA_W - 1 :0] B_real,
    input logic [DATA_W - 1 :0] B_img,
    output logic [DATA_W - 1 : 0] S_real,
    output logic [DATA_W - 1 : 0] S_img,
    output logic overflow 
);
    wire [DATA_W - 1 :0] real_part, img_part, ArBi, BrAi, img_part_inv;
    wire [5:0] over;

    multiplierkarasign #(.DATA_W(DATA_W)) mult1 (
        .A(A_real),
        .B(B_real),
        .S(real_part),
        .overflow(over[0])
    );

    multiplierkarasign #(.DATA_W(DATA_W)) mult2 (
        .A(A_real),
        .B(B_img),
        .S(ArBi),
        .overflow(over[1])
    );

    multiplierkarasign #(.DATA_W(DATA_W)) mult3 (
        .A(B_real),
        .B(A_img),
        .S(BrAi),
        .overflow(over[2])
    );

    multiplierkarasign #(.DATA_W(DATA_W)) mult4 (
        .A(A_img),
        .B(B_img),
        .S(img_part),
        .overflow(over[3])
    );

    assign img_part_inv = {~img_part[DATA_W-1], img_part[DATA_W-2: 0]};

    wire [DATA_W -1  :0] res_real, res_img;

    addersign #(.DATA_W(DATA_W )) addreal(
        .A(real_part),
        .B(img_part_inv),
        .S(res_real),
        .overflow(over[4])
    );

    addersign #(.DATA_W(DATA_W )) addimg(
        .A(ArBi),
        .B(BrAi),
        .S(res_img),
        .overflow(over[5])
    );

    assign S_real = res_real;
    assign S_img = res_img;
    assign overflow = | over;
    
endmodule