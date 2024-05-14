import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from model import *

# https://www.dornerworks.com/blog/setting-vhdl-generics-in-fpga-verification-made-easy-with-cocotb/
@cocotb.test()
async def signextend_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(10):

        A = random.randint(0, 255)
        D_W = dut.DATA_W.value
        E_W = dut.EXT_W.value
        dut.A.value = A

        await Timer(2, units="ns")

        S = sign_extend(A, D_W, D_W + E_W)

        print(bin(A))
        print(bin(dut.A.value))
        print(bin(S))
        print(bin(dut.S.value))
        print()

        # assert dut.X.value == sign_extend(
        #     A, D_W, E_W + D_W
        # ), "Randomised test failed with: {A} = {S}".format(
        #     A=dut.A.value, S=dut.S.value
        # )
        



