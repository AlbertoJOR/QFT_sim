# Quantum Fourier Transform on FPGA

This project implements a fixed-point version of the **Quantum Fourier Transform (QFT)** using Verilog for FPGA simulation and verification. While QFT is originally a quantum algorithm, this implementation emulates its behavior in classical hardware to explore performance, fixed-point arithmetic, and digital signal representation in FPGA environments.

Simulation and verification are done using **Cocotb** (Python-based HDL testbench framework) along with **Verilator** and **GTKWave** for waveform visualization.

---

## Requirements

- **Verilator** or any Verilog/VHDL simulation tool  
  [Official Installation Guide](https://verilator.org/guide/latest/install.html#git-install)

- **GTKWave** (for waveform viewing)
  ```bash
  sudo apt install gtkwave
  ```

- **Python** 3.6 or higher

- **GNU Make** 3 or higher

---

## Installation

### 1. Set up a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install cocotb
```

---

## Running the Simulation

Run the simulation using `make`:

```bash
make
```

This will simulate the QFT module using Verilator and Cocotb, and generate a waveform dump file named `dump.vcd`.

---

## GTKWave Configuration (Optional)

To improve readability of the waveform display in GTKWave, you can adjust font sizes using this command:

```bash
gtkwave -A \
  --rcvar 'fontname_signals Monospace 13' \
  --rcvar 'fontname_waves Monospace 12' \
  dump.vcd signals.gtkw
```
