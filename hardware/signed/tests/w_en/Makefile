TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := n_w_en
MODULE   := w_en

# Waveform for verilator
EXTRA_ARGS += --trace --trace-structs -GN=3

include $(shell cocotb-config --makefiles)/Makefile.sim