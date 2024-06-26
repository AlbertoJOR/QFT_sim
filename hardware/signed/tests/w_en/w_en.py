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


    for i in range (100):
        N = dut.N.value
        sel = random.randint(0, 2**N-1)

        dut.sel.value = sel

        if(i%5 == 0):
            dut.all = 1
        else :
            dut.all = 0


        if(i %7 == 0):
            dut.w_en = 0
        else :
            dut.w_en = 1


        await Timer(10, units="ns")

