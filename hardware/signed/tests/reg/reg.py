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

    for i in range (100):
        D_W = dut.DATA_W.value
        A_real = random.randint(0, 2**D_W-1)
        A_img = random.randint(0, 2**D_W-1)

        dut.A_r.value = A_real
        dut.A_i.value = A_img

        if(i%5 == 0):
            dut.rst = 1
        else :
            dut.rst = 0

        if(i %3 == 0):
            dut.w_en = 1
        else :
            dut.w_en = 0


        await Timer(10, units="ns")

        Sr_add = int(dut.S_r.value)
        Si_add = int(dut.S_r.value)

        print( str(Sr_add) + " + " + str(Si_add)+ "i")
