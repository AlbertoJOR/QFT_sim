TOPLEVEL_LANG ?= verilog
SIM ?= verilator

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/../../hdl/*.sv

TOPLEVEL := signextend
MODULE   := signextend_test

# Waveform for verilator
# EXTRA_ARGS += --trace --trace-structs
EXTRA_ARGS += --trace --trace-structs -GDATA_W=10 -GEXT_W=5

include $(shell cocotb-config --makefiles)/Makefile.sim