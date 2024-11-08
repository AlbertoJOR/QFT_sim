import os
import random
import sys
from pathlib import Path
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from model import *
    from util import *

@cocotb.test()
async def multiplication_randomised_test(dut):
    """Test for karatusuba multiple times"""

    N = dut.N.value
    for i in range(N):

        dut.A.value = i

        await Timer(2, units="ns")

