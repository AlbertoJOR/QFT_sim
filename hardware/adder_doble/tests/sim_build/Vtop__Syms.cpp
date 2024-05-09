// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__pch.h"
#include "Vtop.h"
#include "Vtop___024root.h"

// FUNCTIONS
Vtop__Syms::~Vtop__Syms()
{

    // Tear down scope hierarchy
    __Vhier.remove(0, &__Vscope_adder_doble);
    __Vhier.remove(&__Vscope_adder_doble, &__Vscope_adder_doble__adder_1);
    __Vhier.remove(&__Vscope_adder_doble, &__Vscope_adder_doble__adder_2);

}

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
{
        // Check resources
        Verilated::stackCheck(25);
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-9);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscope_TOP.configure(this, name(), "TOP", "TOP", 0, VerilatedScope::SCOPE_OTHER);
    __Vscope_adder_doble.configure(this, name(), "adder_doble", "adder_doble", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_adder_doble__adder_1.configure(this, name(), "adder_doble.adder_1", "adder_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_adder_doble__adder_2.configure(this, name(), "adder_doble.adder_2", "adder_2", -9, VerilatedScope::SCOPE_MODULE);

    // Set up scope hierarchy
    __Vhier.add(0, &__Vscope_adder_doble);
    __Vhier.add(&__Vscope_adder_doble, &__Vscope_adder_doble__adder_1);
    __Vhier.add(&__Vscope_adder_doble, &__Vscope_adder_doble__adder_2);

    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
        __Vscope_TOP.varInsert(__Vfinal,"A", &(TOP.A), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"B", &(TOP.B), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"X", &(TOP.X), false, VLVT_UINT16,VLVD_OUT|VLVF_PUB_RW,1 ,8,0);
        __Vscope_adder_doble.varInsert(__Vfinal,"A", &(TOP.adder_doble__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,7,0);
        __Vscope_adder_doble.varInsert(__Vfinal,"B", &(TOP.adder_doble__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,7,0);
        __Vscope_adder_doble.varInsert(__Vfinal,"X", &(TOP.adder_doble__DOT__X), false, VLVT_UINT16,VLVD_NODIR|VLVF_PUB_RW,1 ,8,0);
        __Vscope_adder_doble.varInsert(__Vfinal,"X1_o", &(TOP.adder_doble__DOT__X1_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,4,0);
        __Vscope_adder_doble.varInsert(__Vfinal,"X2_o", &(TOP.adder_doble__DOT__X2_o), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,4,0);
        __Vscope_adder_doble__adder_1.varInsert(__Vfinal,"A", &(TOP.adder_doble__DOT__adder_1__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_adder_doble__adder_1.varInsert(__Vfinal,"B", &(TOP.adder_doble__DOT__adder_1__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_adder_doble__adder_1.varInsert(__Vfinal,"Carry", &(TOP.adder_doble__DOT__adder_1__DOT__Carry), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_adder_doble__adder_1.varInsert(__Vfinal,"DATA_W", const_cast<void*>(static_cast<const void*>(&(TOP.adder_doble__DOT__adder_1__DOT__DATA_W))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_adder_doble__adder_1.varInsert(__Vfinal,"X", &(TOP.adder_doble__DOT__adder_1__DOT__X), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,4,0);
        __Vscope_adder_doble__adder_2.varInsert(__Vfinal,"A", &(TOP.adder_doble__DOT__adder_2__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_adder_doble__adder_2.varInsert(__Vfinal,"B", &(TOP.adder_doble__DOT__adder_2__DOT__B), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,3,0);
        __Vscope_adder_doble__adder_2.varInsert(__Vfinal,"Carry", &(TOP.adder_doble__DOT__adder_2__DOT__Carry), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0);
        __Vscope_adder_doble__adder_2.varInsert(__Vfinal,"DATA_W", const_cast<void*>(static_cast<const void*>(&(TOP.adder_doble__DOT__adder_2__DOT__DATA_W))), true, VLVT_UINT32,VLVD_NODIR|VLVF_PUB_RW,1 ,31,0);
        __Vscope_adder_doble__adder_2.varInsert(__Vfinal,"X", &(TOP.adder_doble__DOT__adder_2__DOT__X), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,1 ,4,0);
    }
}
