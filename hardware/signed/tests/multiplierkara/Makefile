TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := multiplierkarasign
MODULE   := multiplierkarasig_test

# Waveform for verilator
# EXTRA_ARGS += --trace --trace-structs
EXTRA_ARGS += --trace --trace-structs -GDATA_W=16

include $(shell cocotb-config --makefiles)/Makefile.sim