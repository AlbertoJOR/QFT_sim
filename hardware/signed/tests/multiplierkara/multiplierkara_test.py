import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from model import *

@cocotb.test()
async def multiplication_randomised_test(dut):
    """Test for karatusuba multiple times"""

    for i in range(500):

        D_W = dut.DATA_W.value
        A = random.randint(0, 2**D_W-1)
        B = random.randint(0, 2**D_W-1)
        dut.A.value = A
        dut.B.value = B

        await Timer(2, units="ns")

        S = multiplication(A, B) 

        assert dut.S.value == S, "Randomised test failed with: {A} * {B} = {S}".format(
            A=dut.A.value, B=dut.B.value, S=dut.S.value
        )
    
@cocotb.test()
async def multiplication_greatest(dut):
    """Test for karatusuba multiple times"""

    D_W = dut.DATA_W.value
    A =  2**D_W-1
    B = 2**D_W-1
    dut.A.value = A
    dut.B.value = B

    await Timer(2, units="ns")

    S = multiplication(A, B) 

    assert dut.S.value == S, "Randomised test failed with: {A} * {B} = {S}".format(
        A=dut.A.value, B=dut.B.value, S=dut.S.value
    )

@cocotb.test()
async def multiplication_middle(dut):
    """Test for karatusuba multiple times"""

    D_W = dut.DATA_W.value
    A =  2**(D_W//2)-1
    B = 2**(D_W//2)-1
    dut.A.value = A
    dut.B.value = B

    await Timer(2, units="ns")

    S = multiplication(A, B) 

    assert dut.S.value == S, "Randomised test failed with: {A} * {B} = {S}".format(
        A=dut.A.value, B=dut.B.value, S=dut.S.value
    )
@cocotb.test()
async def multiplication_zeros(dut):
    """Test for karatusuba multiple times"""

    D_W = dut.DATA_W.value
    A = 0
    B = 0
    dut.A.value = A
    dut.B.value = B

    await Timer(2, units="ns")

    S = multiplication(A, B) 

    assert dut.S.value == S, "Randomised test failed with: {A} * {B} = {S}".format(
        A=dut.A.value, B=dut.B.value, S=dut.S.value
    )


    D_W = dut.DATA_W.value
    A = 0
    B = 2**(D_W//2) -1
    dut.A.value = A
    dut.B.value = B

    await Timer(2, units="ns")

    S = multiplication(A, B) 

    assert dut.S.value == S, "Randomised test failed with: {A} * {B} = {S}".format(
        A=dut.A.value, B=dut.B.value, S=dut.S.value
    )
    
        



