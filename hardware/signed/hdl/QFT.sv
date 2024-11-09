`timescale 1ns/1ps
module QFT #(
    parameter N = 2,
    parameter DATA_W = 32,
    parameter SEL_W = $clog2(N)
)(
    input logic clk, rst,
    // 
    input logic [DATA_W*2 -1 : 0] A_root [N-1:0],
    input logic [DATA_W*2 -1 : 0] A_amp [N-1:0],
    input logic [DATA_W*2 -1 : 0] D_in_root,
    input logic [DATA_W*2 -1 : 0] D_in_amp,
    input logic [SEL_W -1 : 0] addr,
    input logic strt_qft,
    input logic strt_abs,
    //pueden desaparecer
    input logic w_en_mems,
    input logic w_en_new,

    output logic [DATA_W*2 -1 : 0] S_amp [N-1:0],
    output logic [DATA_W*2 -1 : 0] D_out
);
    FSM #(.N(N))FSM(
        .clk(clk),
        .rst(rst),
        .strt_abs(strt_abs),
        .strt_qft(strt_qft),
        .w_en_abs(w_en_abs),
        .w_en_acc(w_en_acc),
        .w_en_mult(w_en_mult),
        .update_state(update_state),
        .sel_counter(sel_counter) 
    );
    wire logic w_en_abs, w_en_acc, w_en_mult, update_state;
    wire logic [SEL_W:0] sel_counter;
    CMEM #(.N(N), .DATA_W(DATA_W)) AMP_MEM(
        .clk(clk),
        .rst(rst),
        .A(A_amp),
        .D_in(D_in_amp),
        .w_en(w_en_mems),
        .new_state(w_en_new||update_state),
        .addr(addr),
        .S(A_amplitudes),
        .D_out(D_out)
    );
    wire [DATA_W*2-1:0] A_amplitudes [N-1:0];


    CMEM #(.N(N), .DATA_W(DATA_W)) ROOT_MEM(
        .clk(clk),
        .rst(rst),
        .A(A_root),
        .D_in(D_in_root),
        .w_en(w_en_mems),
        .new_state(w_en_new),
        .addr(addr),
        .S(A_roots),
        .D_out()
    );

    wire [DATA_W*2-1:0] A_roots [N-1:0];

    indexmod #(.N(N))index(
        .A(sel_counter[SEL_W-1:0]),
        .S(SEL)
    );

    wire[SEL_W-1 : 0]SEL [N-1:0];

    VMux #(.N(N), .DATA_W(DATA_W))IND_MUX(
        .SEL(SEL),
        .A(A_roots),
        .S(COL_roots)
    );
    wire [DATA_W*2-1:0] COL_roots [N-1:0];

    VCMAC2 #(.N(N), .DATA_W(DATA_W))VCMAC(
        .clk(clk),
        .rst(rst),
        .A(A_amplitudes),
        .B(COL_roots),
        .acc(w_en_acc),
        .abs(w_en_abs),
        .w_en_mult(w_en_mult),
        .w_en_acc(w_en_acc),
        .overflow(),
        .S(VMAC_res)
    );
    wire [DATA_W*2-1:0] VMAC_res [N-1:0];
    assign S_amp = VMAC_res;

endmodule