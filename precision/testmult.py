import util as u
import carith as ca


def main():
    a = 0.1419
    b = -0.3464
    c = 0.1249
    d = -0.6234
    DATA_W = 16
    FRACTION_W = DATA_W-2

    a_fixed = u.floatToSignedInt(a, FRACTION_W)
    b_fixed = u.floatToSignedInt(b, FRACTION_W)
    c_fixed = u.floatToSignedInt(c, FRACTION_W)
    d_fixed = u.floatToSignedInt(d, FRACTION_W)
    # a_string = u.fixedPointString(a_fixed, DATA_W, FRACTION_W)
    # b_string = u.fixedPointString(b_fixed, DATA_W, FRACTION_W)
    # print(a_string)
    # print(b_string)
    res_r, res_i = ca.multiplyComplexFixedPoint(a_fixed, b_fixed, c_fixed, d_fixed,FRACTION_W, DATA_W )
    rr_string = u.fixedPointString(res_r, DATA_W, FRACTION_W)
    ri_string = u.fixedPointString(res_i, DATA_W, FRACTION_W)
    u.printComplexFixedPoint(res_r, res_i, DATA_W, FRACTION_W)
    u.printComplexFixedPointTuple((res_r, res_i), DATA_W, FRACTION_W)
    print(rr_string)
    print(ri_string)


    z1 = complex(a, b)
    z2 = complex(c,d)
    result = z1 * z2  # Suma de números complejos
    print(result)

    print("\nAddition")
    res = ca.addComplexFixedPoint(a_fixed, b_fixed, c_fixed, d_fixed,FRACTION_W, DATA_W )
    u.printComplexFixedPointTuple(res, DATA_W, FRACTION_W)
    result = z1 + z2  # Suma de números complejos
    print(result)





if __name__ == "__main__":
    main()

    