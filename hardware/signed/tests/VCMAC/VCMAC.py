import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.clock import Clock

from cocotb.runner import get_runner
from cocotb.triggers import Timer

def fixed_point_array (array_sig, N, D_W):
    data = []
    for i in range(N):
        data.append(fixedPointString(int(array_sig[i].value), D_W, D_W-2))
    return data 

def print_fixed_array(array_sig, name):
    N = len(array_sig)
    print()
    for i in range(N):
        print(name + "[" + str(i) +"] = " + array_sig[i])

def print_fixed_double(array_r, array_i, name):
    N = len(array_r)
    print()
    for i in range(N):
        print(name + "[" + str(i) +"] R = " + array_r[i] +"   "+ "I = " + array_i[i] )

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
    print(dir(dut))

    D_W = dut.DATA_W.value
    N = dut.N.value
    dut.rst.value = 1
    dut.acc.value = 0
    dut.abs.value = 0
    dut.w_en_mult.value = 0
    dut.w_en_acc.value = 0
    for i in range(N):
        dut.A_r[i].value = 0
        dut.A_i[i].value = 0
        dut.B_i[i].value = 0
        dut.B_r[i].value = 0

    await Timer(15, units="ns")

    dut.rst.value = 0




    dut.A_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= floatToSignedInt(1, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.32, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0
    dut.w_en_mult.value = 1

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")

    dut.A_r[0].value= floatToSignedInt(0.9, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= floatToSignedInt(0.3, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.2, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")


    # dut.w_en_mult.value = 0
    # await Timer(10, units="ns")

    print("Sum")

    dut.A_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= floatToSignedInt(1, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.32, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0
    dut.w_en_acc.value = 1
    dut.w_en_mult.value = 0
    dut.acc.value = 1

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")

    await Timer(10, units="ns")

    dut.A_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= floatToSignedInt(1, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.7071067811865475244008443, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.32, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0
    dut.w_en_mult.value = 1
    dut.acc.value = 1
    dut.w_en_acc.value = 0

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")

    dut.A_r[0].value= floatToSignedInt(0.9, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.A_i[0].value= 0
    dut.A_i[1].value= floatToSignedInt(0.3, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.2, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")

    print("doble")
    dut.A_r[0].value= floatToSignedInt(0.5, D_W-2)
    dut.A_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.A_i[0].value= floatToSignedInt(0.8, D_W-2)
    dut.A_i[1].value= floatToSignedInt(0.3, D_W-2)
    dut.B_r[0].value= floatToSignedInt(0.2, D_W-2)
    dut.B_r[1].value= floatToSignedInt(0.4, D_W-2)
    dut.B_i[0].value=  floatToSignedInt(0.5, D_W-2)
    dut.B_i[1].value= 0
    dut.w_en_mult.value = 0
    dut.acc.value = 0
    dut.w_en_acc.value = 0
    dut.abs.value = 1

    await Timer(10, units="ns")

    A_r = fixed_point_array(dut.A_r, N, D_W)
    A_i = fixed_point_array(dut.A_i, N, D_W)
    B_r = fixed_point_array(dut.B_r, N, D_W)
    B_i = fixed_point_array(dut.B_i, N, D_W)
    S_r = fixed_point_array(dut.S_r, N, D_W)
    S_i = fixed_point_array(dut.S_i, N, D_W)

    print_fixed_double(A_r, A_i,"A")
    print_fixed_double(B_r, B_i,"B")
    print_fixed_double(S_r, S_i,"S")




