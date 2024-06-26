TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := top
MODULE   := top

# Waveform for verilator
EXTRA_ARGS += --trace --trace-structs 

include $(shell cocotb-config --makefiles)/Makefile.sim