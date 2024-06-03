import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from complexmodel import *
    from util import *

@cocotb.test()
async def signed_addition_randomised_test(dut):
    """Test for signed addition"""

    for i in range(10):

        D_W = dut.DATA_W.value
        A = random.randint(0, 2**D_W-1)
        B = random.randint(0, 2**D_W-1)

        dut.A.value = A
        dut.B.value = B

        await Timer(2, units="ns")
        A_add = int(dut.A.value)
        B_add = int(dut.B.value)
        S_add = int(dut.S.value)
        over = dut.overflow.value
        A_S = signedString(A_add, D_W)
        B_S = signedString(B_add, D_W)
        S_S = signedString(S_add, D_W)

        print("{} + {} = {}".format(dut.A.value, dut.B.value, dut.S.value))
        print(A_S + " + " + B_S + " = " + S_S + "  o=" + str(over))
