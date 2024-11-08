TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := indexmod
MODULE   := indexmod

# Waveform for verilator
# EXTRA_ARGS += --trace --trace-structs
EXTRA_ARGS += --trace --trace-structs -GN=8

include $(shell cocotb-config --makefiles)/Makefile.sim