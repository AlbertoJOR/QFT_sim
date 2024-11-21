module FSM #(
    parameter  N = 2,
    parameter  WIDTH = $clog2(N),
    parameter MAX = {1'b1, {WIDTH{1'b0}}} // MAX tendrá N bits, todos a 1
    // parameter MAX = {1'b0, {WIDTH{1'b1}}} // MAX tendrá N bits, todos a 1

)(
    input logic clk,
    input logic rst,   
    input logic strt_qft,
    input logic strt_abs,

    output logic w_en_acc,
    output logic w_en_mult,
    output logic w_en_abs,
    output logic update_state,
    output reg [WIDTH:0] sel_counter
);

    // Definición de los estados
    typedef enum reg [2:0] {
        INIT  = 3'b000,
        IDLE  = 3'b001,
        MULT  = 3'b010,
        ACC  = 3'b011,
        ABS  = 3'b100
    } state_t;

    state_t current_state, next_state, prev_state;

    always @(posedge clk or posedge rst) begin
        if (rst) begin 
            current_state <= INIT; 
            prev_state <= INIT;
            // sel_counter <= {(WIDTH+1){1'b0}};
            sel_counter <= 0;
        end else begin
            prev_state <= current_state;
            current_state <= next_state;
            if(current_state == MULT)begin
                sel_counter <= sel_counter + 1;
            end else if(current_state == IDLE) begin
                sel_counter <= 0;
            end
        end 
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
                if(sel_counter < MAX)
                    next_state = MULT;
                else
                    next_state = IDLE;
            end
            ABS : begin
                next_state = IDLE;
            end
            default: next_state = IDLE; // Estado por defecto
        endcase
    end

    // Lógica de salida
    assign  w_en_acc = (current_state == ACC);
    assign  w_en_mult = (current_state == MULT); 
    assign  w_en_abs = (current_state == ABS);
    assign  update_state = (current_state == IDLE && 
            ((prev_state == ACC)||(prev_state == ABS)));

endmodule
