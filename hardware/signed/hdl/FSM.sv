module FSM #(
    parameter integer N = 2,
    parameter integer WIDTH = $clog2(N)

)(
    input logic clk,
    input logic rst,   
    input logic strt_qft,
    input logic strt_abs,

    output logic w_en_acc,
    output logic w_en_mult,
    output logic w_en_abs,
    output logic update_state,
    output reg sel_counter[WIDTH-1:0]
);

    // Definición de los estados
    typedef enum reg [2:0] {
        INIT  = 3'b000,
        IDLE  = 3'b001,
        MULT  = 3'b010,
        ACC  = 3'b011,
        ABS  = 3'b100
    } state_t;

    state_t current_state, next_state;

    always @(posedge clk or posedge rst) begin
        if (rst)
            current_state <= INIT;  
        else
            current_state <= next_state;
    end

    always @(*) begin
        case (current_state)
            INIT: begin
                next_state = IDLE;
            end
            IDLE: begin
                if (strt_qft)
                    next_state = MULT;
                else if(strt_abs)
                    next_state = ABS;
                else
                    next_state = IDLE;
            end
            MULT : begin
                next_state = ACC;
            end
            ACC : begin
                if(sel_counter < N)
                    next_state = MULT;
                else
                    next_state = IDLE;
            end
            ABS : begin
            end
            default: next_state = IDLE; // Estado por defecto
        endcase
    end

    // Lógica de salida (Moore) dependiente del estado actual
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            sel_counter <= 0;
            w_en_acc <= 0;
            w_en_mult 
            w_en_abs,
            update_state,
            state <= INIT;
        end
        else begin
            case (current_state)
                READ: begin
                    w_en <= 0;
                    read <= 1;      // Habilitar `read` en el estado `READ`
                end
                default: begin
                    w_en <= 0;
                    read <= 0;
                end
            endcase
            state <= current_state;
        end
    end

endmodule
