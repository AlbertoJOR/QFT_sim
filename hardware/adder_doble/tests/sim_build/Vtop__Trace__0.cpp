// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_vcd_c.h"
#include "Vtop__Syms.h"


void Vtop___024root__trace_chg_0_sub_0(Vtop___024root* vlSelf, VerilatedVcd::Buffer* bufp);

void Vtop___024root__trace_chg_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_0\n"); );
    // Init
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    if (VL_UNLIKELY(!vlSymsp->__Vm_activity)) return;
    // Body
    Vtop___024root__trace_chg_0_sub_0((&vlSymsp->TOP), bufp);
}

void Vtop___024root__trace_chg_0_sub_0(Vtop___024root* vlSelf, VerilatedVcd::Buffer* bufp) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_0_sub_0\n"); );
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode + 1);
    // Body
    bufp->chgCData(oldp+0,(vlSelf->A),8);
    bufp->chgCData(oldp+1,(vlSelf->B),8);
    bufp->chgSData(oldp+2,(vlSelf->X),9);
    bufp->chgCData(oldp+3,(vlSelf->adder_doble__DOT__A),8);
    bufp->chgCData(oldp+4,(vlSelf->adder_doble__DOT__B),8);
    bufp->chgSData(oldp+5,(vlSelf->adder_doble__DOT__X),9);
    bufp->chgCData(oldp+6,(vlSelf->adder_doble__DOT__X1_o),5);
    bufp->chgCData(oldp+7,(vlSelf->adder_doble__DOT__X2_o),5);
    bufp->chgCData(oldp+8,(vlSelf->adder_doble__DOT__adder_1__DOT__A),4);
    bufp->chgCData(oldp+9,(vlSelf->adder_doble__DOT__adder_1__DOT__B),4);
    bufp->chgBit(oldp+10,(vlSelf->adder_doble__DOT__adder_1__DOT__Carry));
    bufp->chgCData(oldp+11,(vlSelf->adder_doble__DOT__adder_1__DOT__X),5);
    bufp->chgCData(oldp+12,(vlSelf->adder_doble__DOT__adder_2__DOT__A),4);
    bufp->chgCData(oldp+13,(vlSelf->adder_doble__DOT__adder_2__DOT__B),4);
    bufp->chgBit(oldp+14,(vlSelf->adder_doble__DOT__adder_2__DOT__Carry));
    bufp->chgCData(oldp+15,(vlSelf->adder_doble__DOT__adder_2__DOT__X),5);
}

void Vtop___024root__trace_cleanup(void* voidSelf, VerilatedVcd* /*unused*/) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_cleanup\n"); );
    // Init
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VlUnpacked<CData/*0:0*/, 1> __Vm_traceActivity;
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        __Vm_traceActivity[__Vi0] = 0;
    }
    // Body
    vlSymsp->__Vm_activity = false;
    __Vm_traceActivity[0U] = 0U;
}
