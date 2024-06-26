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
    j= 0

    for i in range (100):
        if(i%2==0):
            dut.gate_sel.value = j%11
            dut.row_sel.value = 0
        else:
            dut.gate_sel.value = (j)%11
            dut.row_sel.value = 1
            j = j+1

        await Timer(10, units="ns")

