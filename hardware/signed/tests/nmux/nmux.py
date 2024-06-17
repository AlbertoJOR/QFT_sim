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

    # cocotb.fork(clock_generator(dut.clk))
    D_W = dut.DATA_W.value
    N = dut.N.value
    print("parameters:")
    print(N)
    print(D_W)

    for i in range (100):
        sel = random.randint(0, N-1)
        dut.sel.value = sel
        for i in range(N):
            dut.A[i].value = random.randint(0,2**D_W-1)
        

        await Timer(10, units="ns")

        S = int(dut.S.value)

        print("sel = "+ str(sel) + "  S = " + str(S))
        
