import carith as ca
import util as u


vector = ca.modularExponentiationVectorCFP(7, 15, 4, 12)
u.printComplexFixedVectorShor(vector, 14, 12, 4)

# vectorRand = ca.randomNormComplexFixedPVector(2**2, 12)
# u.printComplexFixedVectorQuantum(vectorRand,14,12)

vectorQFT = ca.qftTensorCFP(vector, 4, 12, 14)
u.printComplexFixedVectorShor(vectorQFT,14,12,4)