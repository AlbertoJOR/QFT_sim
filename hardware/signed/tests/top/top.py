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

@cocotb.test()
async def complex_adder_randomised_test(dut):
    """Test for complex multiplication times"""

    # cocotb.fork(clock_generator(dut.clk))

    for i in range (100):
        D_W = 32
        A = random.randint(0, 2**D_W-1)

        dut.A.value = A

        await Timer(10, units="ns")

        S = int(dut.S.value)

        print(str(S))
