import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.clock import Clock

from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from util import *

@cocotb.coroutine
async def clock_generator(clock):
    while True:
        clock <= 0
        await Timer(5, units="ns")  # Half period, 5 ns in this case
        clock <= 1
        await Timer(5, units="ns")  

@cocotb.test()
async def complex_adder_randomised_test(dut):
    """Test for complex multiplication times"""

    cocotb.fork(clock_generator(dut.clk))

    D_W = dut.DATA_W.value
    dut.rst.value = 1
    dut.sum.value = 0
    dut.abs.value = 0
    dut.sel.value = 0
    dut.w_en.value = 0
    dut.A_r[0].value= 0
    dut.A_r[1].value= 0
    dut.A_i[0].value= 0
    dut.A_i[1].value= 0
    dut.B_r[0].value= 0
    dut.B_r[1].value= 0
    dut.B_i[0].value= 0
    dut.B_i[1].value= 0

    await Timer(15, units="ns")

    Ar0_F = fixedPointString(int(dut.A_r[0].value), D_W, D_W-2)
    Ar1_F = fixedPointString(int(dut.A_r[1].value), D_W, D_W-2)
    Br0_F = fixedPointString(int(dut.B_r[0].value), D_W, D_W-2)
    Br1_F = fixedPointString(int(dut.B_r[1].value), D_W, D_W-2)
    Sr0_F = fixedPointString(int(dut.S_r[0].value), D_W, D_W-2)
    Sr1_F = fixedPointString(int(dut.S_r[1].value), D_W, D_W-2)
    print("Ar0 = " + Ar0_F + " Ar1 = " + Ar1_F)
    print("Br0 = " + Br0_F + " Br1 = " + Br1_F)
    print("Sr0 = " + Sr0_F + " Sr1 = " + Sr1_F)
    print()


    dut.rst.value = 0
    dut.A_r[0].value= floatToSignedInt(1, D_W-2)
    dut.A_r[1].value= 0
    dut.A_i[0].value= 0
    dut.A_i[1].value= 0
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_i[0].value= 0
    dut.B_i[1].value= 0
    dut.w_en.value = 1

    await Timer(10, units="ns")

    Ar0_F = fixedPointString(int(dut.A_r[0].value), D_W, D_W-2)
    Ar1_F = fixedPointString(int(dut.A_r[1].value), D_W, D_W-2)
    Br0_F = fixedPointString(int(dut.B_r[0].value), D_W, D_W-2)
    Br1_F = fixedPointString(int(dut.B_r[1].value), D_W, D_W-2)
    Sr0_F = fixedPointString(int(dut.S_r[0].value), D_W, D_W-2)
    Sr1_F = fixedPointString(int(dut.S_r[1].value), D_W, D_W-2)
    print("Ar0 = " + Ar0_F + " Ar1 = " + Ar1_F)
    print("Br0 = " + Br0_F + " Br1 = " + Br1_F)
    print("Sr0 = " + Sr0_F + " Sr1 = " + Sr1_F)
    print()

    dut.A_r[0].value= floatToSignedInt(1, D_W-2)
    dut.A_r[1].value= 0
    dut.A_i[0].value= 0
    dut.A_i[1].value= 0
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(-0.7071067811865475244008443, D_W-2)
    dut.B_i[0].value= 0
    dut.B_i[1].value= 0

    await Timer(10, units="ns")

    Ar0_F = fixedPointString(int(dut.A_r[0].value), D_W, D_W-2)
    Ar1_F = fixedPointString(int(dut.A_r[1].value), D_W, D_W-2)
    Br0_F = fixedPointString(int(dut.B_r[0].value), D_W, D_W-2)
    Br1_F = fixedPointString(int(dut.B_r[1].value), D_W, D_W-2)
    Sr0_F = fixedPointString(int(dut.S_r[0].value), D_W, D_W-2)
    Sr1_F = fixedPointString(int(dut.S_r[1].value), D_W, D_W-2)
    print("Ar0 = " + Ar0_F + " Ar1 = " + Ar1_F)
    print("Br0 = " + Br0_F + " Br1 = " + Br1_F)
    print("Sr0 = " + Sr0_F + " Sr1 = " + Sr1_F)
    print()

    dut.rst.value = 0
    dut.A_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= 0
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_i[0].value= 0
    dut.B_i[1].value= 0
    dut.w_en.value = 1

    await Timer(10, units="ns")

    Ar0_F = fixedPointString(int(dut.A_r[0].value), D_W, D_W-2)
    Ar1_F = fixedPointString(int(dut.A_r[1].value), D_W, D_W-2)
    Br0_F = fixedPointString(int(dut.B_r[0].value), D_W, D_W-2)
    Br1_F = fixedPointString(int(dut.B_r[1].value), D_W, D_W-2)
    Sr0_F = fixedPointString(int(dut.S_r[0].value), D_W, D_W-2)
    Sr1_F = fixedPointString(int(dut.S_r[1].value), D_W, D_W-2)
    print("Ar0 = " + Ar0_F + " Ar1 = " + Ar1_F)
    print("Br0 = " + Br0_F + " Br1 = " + Br1_F)
    print("Sr0 = " + Sr0_F + " Sr1 = " + Sr1_F)
    print()

    dut.A_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= 0
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(-0.7071067811865475244008443, D_W-2)
    dut.B_i[0].value= 0
    dut.B_i[1].value= 0

    await Timer(10, units="ns")

    Ar0_F = fixedPointString(int(dut.A_r[0].value), D_W, D_W-2)
    Ar1_F = fixedPointString(int(dut.A_r[1].value), D_W, D_W-2)
    Br0_F = fixedPointString(int(dut.B_r[0].value), D_W, D_W-2)
    Br1_F = fixedPointString(int(dut.B_r[1].value), D_W, D_W-2)
    Sr0_F = fixedPointString(int(dut.S_r[0].value), D_W, D_W-2)
    Sr1_F = fixedPointString(int(dut.S_r[1].value), D_W, D_W-2)
    print("Ar0 = " + Ar0_F + " Ar1 = " + Ar1_F)
    print("Br0 = " + Br0_F + " Br1 = " + Br1_F)
    print("Sr0 = " + Sr0_F + " Sr1 = " + Sr1_F)
    print()
