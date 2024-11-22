#### Khalil 2015 Pipeline implementation

Stratix III EP3SL150F1152C2 FPGA
For example for the 3 qubit is implemented using the tensor product of the gate and the identity, so the pipe lines are designed for each of this matrices.

| Qubits                    | 2 s   | 2 p   | 3 s   | 3 p   | 4 s   | 4 p   | 5 s   | 5 p   |
| ------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Combinational ALUTs       | 288   | 469   | 948   | 1381  | 2776  | 4185  | 33904 | 34365 |
| Dedicated Logic Registers | 680   | 139   | 2176  | 276   | 6528  | 548   | 18496 | 1093  |
| DSP Block 18-bit Element  | 32    | 32    | 104   | 104   | 320   | 316   | 384   | 384   |
| Frecuency                 | 192.2 | 146.4 | 178.0 | 130.0 | 156.0 | 110.1 | 145.1 | 102.1 |

S : serial, P : pipelined

#### Qian Yu 2019 QFT binary decomposition pipeline

Altera Stratix IV EP4SGX180FF35C4
Decomposition of QFTn = (I x QFTn/2) LB (QFTn/2 x I) it can be preformed recursively. QFT-4 requieres 10 pipeline a linking block and it is a acumulator. 14 18 22 mantissa.

| Qubits              | 2     | 4     | 5     | 8     |
| ------------------- | ----- | ----- | ----- | ----- |
| Combinational ALUTs | 390   | 2960  | 96128 | 13035 |
| Logic Registers     | 352   | 1032  | 2816  | 31961 |
| DSP-18              | 64    | 32    | 1024  | 128   |
| Precision %         | 0.000 | 0.000 | 0.007 | 0.001 |

Software simulation based on Matlab R2018a is conducted on a 3.40 GHz Intel Core i7-6800K processor.

|         | Simulation (s) | Emulation (s) |
| ------- | -------------- | ------------- |
| 4-qubit | 9.3×10-6       | 4.8×10-8      |
| 8-qubit | 6.1×10-5       | 1.2×10-6      |

#### Silva A 2017 HLS QFT implementation

ZYNQ7000
It uses the tools of the QFT hls math implementes a 32 float operation calculating the cos and sin/ sqrt it is calculated using the matrix

| Qubits       | 1    | 2     | 3      | 4      | 5       | 6       |
| ------------ | ---- | ----- | ------ | ------ | ------- | ------- |
| LUT(%)       | 9    | 18    | 39     | 55     | 175     | 399     |
| LUTs         | 4788 | 9576  | 20748  | 29260  | 93100   | 212268  |
| FPGA(us)     | 1.17 | 1.56  | 2.35   | 3.91   | 8.78    | 115.47  |
| arm zynq(us) | 6.18 | 21.67 | 101.53 | 436.06 | 1836.41 | 7609.74 |

#### WAIDYASOORIYA H 2022 OpenCL MUltiple FPGA HBM

Stratix 10 MX
The hardware implementation is described like a HLS but for Inter Quartus OpenCL en Intel FPGA, a single presición is used

| Qubits          | 20            | 21            | 22            | 23            | 24            | 25            | 26            | 27            | 28            | 29            |
| --------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Logic           | 306,782 (44%) | 309,186 (44%) | 316,823 (45%) | 322,266 (46%) | 325,364 (46%) | 327,185 (47%) | 328,310 (47%) | 325,005 (46%) | 331,912 (47%) | 331,238 (47%) |
| Registers       | 672,713       | 680,786       | 684,676       | 693,077       | 703,402       | 710,937       | 717,952       | 722,814       | 733,189       | 742,779       |
| DSP blocks      | 1,008 (25%)   | 1,040 (26%)   | 1,072 (27%)   | 1,104 (28%)   | 1,136 (29%)   | 1,168 (29%)   | 1,200 (30%)   | 1,232 (31%)   | 1,264 (32%)   | 1,296 (33%)   |
| RAM blocks      | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   | 1,513 (22%)   |
| SRAM (MB)       | 2.03 (12%)    | 2.04 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    | 2.05 (12%)    |
| DRAM (MB)       | 16            | 32            | 64            | 128           | 256           | 512           | 1,024         | 2,048         | 4,096         | 8,192         |
| Frequency (MHz) | 299           | 295           | 294           | 294           | 286           | 286           | 300           | 300           | 300           | 300           |

#### Rivera J 2011 Hardware Emulation of Quantum Fourier Transform

Pipeline quantum hardware implementation of QFT n stages, the Quantum gates of controled rotattion and hadamard are implemented in hardware fiexed point of 18 bits. FPGA FPGA EP25180F1508I4

| Qubits       | 2      | 4      | 6      | 8      | 10     | 12     | 14    | 16    |
| ------------ | ------ | ------ | ------ | ------ | ------ | ------ | ----- | ----- |
| S ALUTs      | 239    | 500    | 833    | 1165   | 1498   | 1758   | 2090  | 15228 |
| P ALUTs      | 239    | 436    | 777    | 969    | 1241   | 1439   | 1711  | 14786 |
| S Registers  | 181    | 326    | 471    | 615    | 760    | 904    | 1048  | 2128  |
| P Registers  | 289    | 726    | 946    | 1167   | 1390   | 1613   | 1837  | 3537  |
| S DSP 9-bit  | 16     | 56     | 128    | 232    | 368    | 536    | 736   | 768   |
| P DSP 9-bit  | 16     | 56     | 128    | 232    | 368    | 536    | 736   | 768   |
| S Freq (MHz) | 109.10 | 49.50  | 30.75  | 22.28  | 17.27  | 14.04  | 11.70 | 10.17 |
| P Freq (MHz) | 150.40 | 136.30 | 116.86 | 111.83 | 112.85 | 103.84 | 97.30 | 83.10 |

S: serial, P : pipelined

#### Moe T 2019 Implementation and Analysis of Quantum Fourier Transform Gates Over FPGA Framework

It implementes the matrix multiplication, a convolution for 1 to 3 qubit QFT. 16 fixed signed bit. the implementation is made in an Artix 7

| Qubits | 1   | 2    | 3    |
| ------ | --- | ---- | ---- |
| LUTs   | 150 | 403  | 1140 |
| SLRs   | 49  | 117  | 265  |
| Cells  | 561 | 1399 | 3685 |

#### Lee Y 2019 FPGA-Based Quantum Circuit Emulation: A Case Study on Quantum Fourier Transform

Iplements it in 2^n secuential stages, ithink it is the matrix. with 26 bit fixed point
Altera Stratix IV EP4SGX530KF43C4 FPGA

| Qubit     | 2     | 5      |
| --------- | ----- | ------ |
| ALUTs     | 458   | 128080 |
| Registers | 416   | 3328   |
| DSP 18bit | 64    | 1024   |
| Error(%)  | 0.000 | 0.001  |

#### Naveed Mahmud 2018 Scalable High-Precision and High-Throughput Architecture for Emulation of Quantum Algorithms

single prescicion implementa compuertas. cada operacion hace la compuerta con swap y el producto tensorial y regresa el qubit a su posición anterior. va compuerta a compueta y es todo secuancial

Arria 10

| FPGA Resource         | 2-qubit      | 3-qubit       | 4-qubit       |
| --------------------- | ------------ | ------------- | ------------- |
| Logic utilization ALM | 67,735 (16%) | 108,833 (25%) | 266,835 (63%) |
| RAM blocks            | 299 (11%)    | 578 (21%)     | 1,651 (61%)   |
| DSP Blocks            | 72 (5%)      | 108 (7%)      | 524 (35%)     |
| Freq(MHz)             | 233          | 233           | 233           |

## Algorithms that utilizes the Quantum Fouriere Transform

1. Phase estimation algorithm [1]: it is used to calculate the
   eigenvalues of a unitary operator. This algorithm presents
   advantages in quantum chemistry because it speeds up the
   calculation of molecular orbital energies.
2. Shor’s factoring algorithm [1]: it is based on the phase
   estimation algorithm, and allows to find exponentially faster
   the prime factors of a very big n-bit integer number.
3. Period finding algorithm [1]: it allows to find the period
   of a periodic function. It is at the heart of the Shor’s algorithm
   for the discrete logarithm.
4. Shor’s algorithm for the discrete logarithm [1]: it is
   useful to solve the problem of finding s when a and b are
   known in the expression ܾ ൌ ܽݏ. This algorithm is
   fundamental in cryptography.
5. Feature selection algorithm [2]: it performs feature
   selection tasks more quickly than its classic counterpart. This
   algorithm is used for pattern and image recognition.
