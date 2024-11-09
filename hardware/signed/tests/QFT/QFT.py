import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.clock import Clock

from cocotb.runner import get_runner
from cocotb.triggers import Timer
import random
import numpy as np



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
async def QFT_randomised_test(dut):
    """Test for complex multiplication times"""

    cocotb.fork(clock_generator(dut.clk))
    print(dir(dut))

    D_W = dut.DATA_W.value
    N = dut.N.value
    valores = np.arange(0.0, 0.26, 0.01)

    dut.rst.value = 1

    dut.strt_qft.value = 0
    dut.strt_abs.value = 0
    dut.w_en_mems.value = 0
    dut.w_en_new.value = 0
    dut.D_in_root.value = 0
    dut.D_in_amp.value = 0
    dut.addr.value = 0
    for i in range(N):
        dut.A_root[i].value = 0
        dut.A_amp[i].value = 0
   
    await Timer(35, units="ns")
    dut.rst.value = 0

    dut.w_en_new.value = 1
    for i in range(N):
        dut.A_root[i].value = ComplexFloatToSignedInt(random.choice(valores), random.choice(valores), D_W-2, D_W)
        dut.A_amp[i].value = ComplexFloatToSignedInt(random.choice(valores), random.choice(valores), D_W-2, D_W)

    await Timer(10, units="ns")
    dut.w_en_new.value = 0
    dut.strt_qft.value = 1
    await Timer(10, units="ns")
    dut.strt_qft.value = 0

    await Timer(200, units="ns")








