`timescale 1ns/1ps
module ckarasign #(
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
    wire [DATA_W - 1 :0] real_part, img_part, Asum, Bsum, AB, img_part_inv, neg_part;
    wire over[7 : 0];
    

    multiplierkarasign #(.DATA_W(DATA_W)) mult1 (
        .A(A_real),
        .B(B_real),
        .S(real_part),
        .overflow(over[0])
    );


    multiplierkarasign #(.DATA_W(DATA_W)) mult2 (
        .A(A_img),
        .B(B_img),
        .S(img_part),
        .overflow(over[1])
    );

    assign img_part_inv = {~img_part[DATA_W-1], img_part[DATA_W-2: 0]};

    wire [DATA_W -1  :0] res_real, res_img;

    addersign #(.DATA_W(DATA_W )) addreal(
        .A(real_part),
        .B(img_part_inv),
        .S(S_real),
        .overflow(over[2])
    );

    addersign #(.DATA_W(DATA_W )) adderA(
        .A(A_img),
        .B(A_real),
        .S(Asum),
        .overflow(over[3])
    );

    addersign #(.DATA_W(DATA_W )) adderB(
        .A(B_img),
        .B(B_real),
        .S(Bsum),
        .overflow(over[4])
    );

    multiplierkarasign #(.DATA_W(DATA_W)) mult3 (
        .A(Asum),
        .B(Bsum),
        .S(AB),
        .overflow(over[5])
    );

    addersign #(.DATA_W(DATA_W )) sumneg(
        .A({~real_part[DATA_W-1], real_part[DATA_W-2:0]}),
        .B({~img_part[DATA_W-1], img_part[DATA_W-2:0]}),
        .S(neg_part),
        .overflow(over[6])
    );

    addersign #(.DATA_W(DATA_W )) adderimg(
        .A(neg_part),
        .B(AB),
        .S(S_img),
        .overflow(over[7])
    );


    assign overflow = over[0] | over[1] | over[2] | over[3] | over[4] | over[5] | over[6] | over[7];
    
endmodule