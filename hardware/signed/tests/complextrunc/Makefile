TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := cmultipliertrunc
MODULE   := cmultiplier_test

# Waveform for verilator
EXTRA_ARGS += --trace --trace-structs -GDATA_W=4

include $(shell cocotb-config --makefiles)/Makefile.sim