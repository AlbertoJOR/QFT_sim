import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from util import *

@cocotb.test()
async def complex_adder_randomised_test(dut):
    """Test for complex multiplication times"""

    for i in range(10):

        D_W = dut.DATA_W.value
        A_real = random.randint(0, 2**D_W-1)
        A_img = random.randint(0, 2**D_W-1)
        B_real = random.randint(0, 2**D_W-1)
        B_img = random.randint(0, 2**D_W-1)

        dut.A_real.value = A_real
        dut.A_img.value = A_img
        dut.B_real.value = B_real
        dut.B_img.value = B_img

        await Timer(2, units="ns")

        Ar_add = int(dut.A_real.value)
        Br_add = int(dut.B_real.value)
        Sr_add = int(dut.S_real.value)
        over = dut.overflow.value
        Ar_S = signedString(Ar_add, D_W)
        Br_S = signedString(Br_add, D_W)
        Sr_S = signedString(Sr_add, D_W)
        Ar_F = fixedPointString(Ar_add, D_W, D_W-2)
        Br_F = fixedPointString(Br_add, D_W, D_W-2)
        Sr_F = fixedPointString(Sr_add, D_W, D_W-2)

        Ai_add = int(dut.A_img.value)
        Bi_add = int(dut.B_img.value)
        Si_add = int(dut.S_img.value)
        Ai_S = signedString(Ai_add, D_W)
        Bi_S = signedString(Bi_add, D_W)
        Si_S = signedString(Si_add, D_W)
        Ai_F = fixedPointString(Ai_add, D_W, D_W-2)
        Bi_F = fixedPointString(Bi_add, D_W, D_W-2)
        Si_F = fixedPointString(Si_add, D_W, D_W-2)


        print("(" + Ar_S + " + " + Ai_S+ "i) + " + "(" + Br_S + " + " + Bi_S+ "i)" + " = " + "(" + Sr_S + " + " + Si_S+ "i)"  + "  o=" + str(over))
        print("(" + Ar_F + " + " + Ai_F+ "i) + " + "(" + Br_F + " + " + Bi_F+ "i)" + " = " + "(" + Sr_F + " + " + Si_F+ "i)"  + "  o=" + str(over))
        print()
