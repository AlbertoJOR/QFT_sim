module multiplierkara #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 : 0] A,
    input logic [DATA_W - 1 : 0] B,
    input logic [DATA_W * 2 - 1 : 0] S
);
    multiplier #(.DATA_W(DATA_W)) mult1 (
        .A(),
        .B(),
        .S(),
    );

    multiplier mult2 (
        .A(),
        .B(),
        .S(),
    );

    multiplier mult3 (
        .A(),
        .B(),
        .S(),
    );
endmodule