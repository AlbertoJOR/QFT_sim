# Requisitos
- verilator o una herramienta de simulación de verilog o VHDL
https://verilator.org/guide/latest/install.html#git-install
- gtkwave
```
apt install gtkwave
```
- python 3.6+
- GNU make 3+

# Installación
## Crear un ambiente 
```
python3 -m venv venv
source venv/bin/activate
```

```
pip install cocotb
```
Comando para cambiar el tamaño de las ondas, igual se puede modificar el archivo ~/.gtkwaverc
```
gtkwave -A --rcvar 'fontname_signals Monospace 13' --rcvar 'fontname_waves Monospace 12' dump.vcd signals.gtkw 
```