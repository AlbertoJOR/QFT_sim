`timescale 1ns/1ps

module addersign #(
    parameter integer DATA_W = 32
)(
    input logic [DATA_W -1 :0] A,
    input logic [DATA_W -1 :0] B,
    output logic [DATA_W - 1 :0] S,
    output logic overflow
);
    // |Sing bit| Decimal bit| 30 bit fraction|
    wire [DATA_W -1 : 0] Aex, Bex, As, Bs, Ainv, Binv;
    wire Asig, Bsig, Ssig, Adec, Bdec, oflow, diffsig, compare;
    wire [DATA_W -1: 0]  sum;
    wire [DATA_W -2 : 0] suminv;

    assign Aex ={1'b0, A[DATA_W -2 :0]};
    assign Bex ={1'b0, B[DATA_W -2 :0]};


    inverter #(.DATA_W(DATA_W)) invA(
        .A(Aex),
        .S(Ainv)
    );

    inverter #(.DATA_W(DATA_W)) invB(
        .A(Bex),
        .S(Binv)
    );

    assign Asig = A[DATA_W -1];
    assign Bsig = B[DATA_W -1];
    assign Adec = A[DATA_W -2];
    assign Bdec = B[DATA_W -2];

    assign diffsig = Asig ^ Bsig;

    assign As = Asig & diffsig? Ainv : Aex;
    assign Bs = Bsig & diffsig? Binv : Bex;

    assign compare = Aex > Bex;

    assign Ssig = diffsig & ((compare & Asig) | (~compare & Bsig)) | (Asig & Bsig);

    assign sum = As + Bs;
    assign oflow = (Adec & Bdec) & (Asig ~^ Bsig) | sum[DATA_W-1] & ~diffsig;
    assign overflow = oflow;

    inverter #(.DATA_W(DATA_W-1)) invS(
        .A(sum[DATA_W-2 : 0]),
        .S(suminv)
    );

    assign S = overflow ? {DATA_W{1'b1}} : Ssig & diffsig ?{Ssig, suminv}: {Ssig, sum[DATA_W -2 :0]};


    
    
endmodule