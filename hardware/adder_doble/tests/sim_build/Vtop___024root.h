// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(A,7,0);
    VL_IN8(B,7,0);
    CData/*7:0*/ adder_doble__DOT__A;
    CData/*7:0*/ adder_doble__DOT__B;
    CData/*4:0*/ adder_doble__DOT__X1_o;
    CData/*4:0*/ adder_doble__DOT__X2_o;
    CData/*3:0*/ adder_doble__DOT__adder_1__DOT__A;
    CData/*3:0*/ adder_doble__DOT__adder_1__DOT__B;
    CData/*0:0*/ adder_doble__DOT__adder_1__DOT__Carry;
    CData/*4:0*/ adder_doble__DOT__adder_1__DOT__X;
    CData/*3:0*/ adder_doble__DOT__adder_2__DOT__A;
    CData/*3:0*/ adder_doble__DOT__adder_2__DOT__B;
    CData/*0:0*/ adder_doble__DOT__adder_2__DOT__Carry;
    CData/*4:0*/ adder_doble__DOT__adder_2__DOT__X;
    CData/*0:0*/ __VstlFirstIteration;
    CData/*0:0*/ __VicoFirstIteration;
    CData/*0:0*/ __VactContinue;
    VL_OUT16(X,8,0);
    SData/*8:0*/ adder_doble__DOT__X;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<1> __VstlTriggered;
    VlTriggerVec<1> __VicoTriggered;
    VlTriggerVec<0> __VactTriggered;
    VlTriggerVec<0> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // PARAMETERS
    static constexpr IData/*31:0*/ adder_doble__DOT__adder_1__DOT__DATA_W = 4U;
    static constexpr IData/*31:0*/ adder_doble__DOT__adder_2__DOT__DATA_W = 4U;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
