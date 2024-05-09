module inverter #(
    parameter integer DATA_W = 32
) (
    input logic [DATA_W - 1 : 0] A,
    output logic [DATA_W - 1 : 0] B
);
    wire [DATA_W : 0] sum;
    wire [DATA_W -1 :0] notA;
    assign notA = ~A;
    wire [DATA_W-1:0] one_cte = { {DATA_W-1{1'b0}}, 1'b1} ;
    assign sum = notA + one_cte;
    assign B = sum[DATA_W-1:0];
endmodule