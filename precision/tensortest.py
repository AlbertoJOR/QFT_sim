import carith as ca
import util as u


FRACTION_WIDTH = 12
DATA_WIDTH = 16
MA = u.randComplexMatrix(2,2, FRACTION_WIDTH)
MB = u.randComplexMatrix(2,2,FRACTION_WIDTH)
u.printComplexFixedMatrix(MA,DATA_WIDTH, FRACTION_WIDTH)
u.printComplexFixedMatrix(MB,DATA_WIDTH, FRACTION_WIDTH)
Res = ca.tensorProductComplexFixed(MA, MB, FRACTION_WIDTH, DATA_WIDTH)
u.printComplexFixedMatrix(Res, DATA_WIDTH, FRACTION_WIDTH)