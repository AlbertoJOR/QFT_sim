module gates_1Q #(
    parameter integer DATA_W = 32
) (
    input logic [3:0] gate_sel,
    input logic row_sel,
    output logic [DATA_W*4-1:0] gate_row
);
    wire [DATA_W*4*11-1:0] gate_row_aux;
    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h00000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h00000000),
        .D3i(32'h00000000)
    )G_zero(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4-1:0])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h40000000),
        .D3i(32'h00000000)
    )G_sigma0(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*2-1:DATA_W*4])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h00000000),
        .D0i(32'h00000000),
        .D1r(32'h40000000),
        .D1i(32'h00000000),
        .D2r(32'h40000000),
        .D2i(32'h00000000),
        .D3r(32'h00000000),
        .D3i(32'h00000000)
    )G_sigmaX(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*3-1:DATA_W*4*2])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h00000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'hC0000000),
        .D2r(32'h00000000),
        .D2i(32'h40000000),
        .D3r(32'h00000000),
        .D3i(32'h00000000)
    )G_sigmaY(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*4-1:DATA_W*4*3])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h00000000),
        .D3i(32'hC0000000)
    )G_sigmaZ(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*5-1:DATA_W*4*4])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h2D413CCD),
        .D0i(32'h00000000),
        .D1r(32'h2D413CCD),
        .D1i(32'h00000000),
        .D2r(32'h2D413CCD),
        .D2i(32'h00000000),
        .D3r(32'hAD413CCD),
        .D3i(32'h00000000)
    )G_H(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*6-1:DATA_W*4*5])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h00000000),
        .D3i(32'h40000000)
    )G_S(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*7-1:DATA_W*4*6])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h00000000),
        .D3i(32'hC0000000)
    )G_Sd(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*8-1:DATA_W*4*7])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h2D413CCD),
        .D3i(32'h2D413CCD)
    )G_T(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*9-1:DATA_W*4*8])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h40000000),
        .D0i(32'h00000000),
        .D1r(32'h00000000),
        .D1i(32'h00000000),
        .D2r(32'h00000000),
        .D2i(32'h00000000),
        .D3r(32'h2D413CCD),
        .D3i(32'hAD413CCD)
    )G_Td(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*10-1:DATA_W*4*9])
    );

    ROM1QGate #(
        .DATA_W(DATA_W),
        .D0r(32'h20000000),
        .D0i(32'h20000000),
        .D1r(32'h20000000),
        .D1i(32'hA0000000),
        .D2r(32'h20000000),
        .D2i(32'hA0000000),
        .D3r(32'h20000000),
        .D3i(32'h20000000)
    )G_sqrtX(
        .addr(row_sel),
        .gate_row(gate_row_aux[DATA_W*4*11-1:DATA_W*4*10])
    );

    mul_mux #(.N(11), .DATA_W(DATA_W*4))mux(
        .A(gate_row_aux),
        .sel(gate_sel),
        .S(gate_row)
    );
endmodule