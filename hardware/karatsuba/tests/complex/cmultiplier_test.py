import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from complexmodel import *

@cocotb.test()
async def complex_multiplication_randomised_test(dut):
    """Test for complex multiplication times"""

    for i in range(100000):

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

        S = complex_mul(A_real, A_img, B_real, B_img, D_W) 
        S_real = S[0]
        S_img = S[1]

        assert dut.S_real.value == S_real, "Randomised test failed real part with: ({A1} + {A2}i) * ({B1} + {B2}i) = {S1} + {S2}i \n ({A1i} + {A2i}i) * ({B1i} + {B2i}i) = {S1i} + {S2i}i \n {Ss1} {Ss2}".format(
            A1=int(dut.A_real.value), A2=int(dut.A_img.value), B1=int(dut.B_real.value), B2=int(dut.B_img.value), S1=int(dut.S_real.value), S2=int(dut.S_img.value),
            A1i=dut.A_real.value, A2i=dut.A_img.value, B1i=dut.B_real.value, B2i=dut.B_img.value, S1i=dut.S_real.value, S2i=dut.S_img.value, Ss1 = S_real , Ss2 = S_img
        )
    
        assert dut.S_img.value == S_img, "Randomised test failed imaginary part with: ({A1} + {A2}i) * ({B1} + {B2}i) = {S1} + {S2}i".format(
            A1=dut.A_real.value, A2=dut.A_img.value, B1=dut.B_real.value, B2=dut.B_img.value, S1=dut.S_real.value, S2=dut.S_img.value
        )