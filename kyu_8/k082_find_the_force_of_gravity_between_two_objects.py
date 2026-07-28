"""
Find the force of gravity between two objects

Your job is to find the gravitational force between two spherical objects (obj1 , obj2).

input
Two arrays are given :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg)
gram (g)
milligram (mg)
microgram (μg)
pound (lb)
distance units are :

meter (m)
centimeter (cm)
millimeter (mm)
micrometer (μm)
feet (ft)
Note
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution
"""
import math


def assert_approx_equals(actual, expected, rel_tol=1e-9, abs_tol=0.0):
    if not math.isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol):
        raise AssertionError(f"Expected {expected}, actual {actual}")


def solution(arr_val, arr_unit):
    # Gravitational constant G
    G = 6.67e-11

    # Dictionary of conversion factors for mass to kilograms (kg)
    mass_conv = {
        "kg": 1.0,
        "g": 1e-3,
        "mg": 1e-6,
        "μg": 1e-9,
        "lb": 0.453592
    }

    # Dictionary of conversion factors for distances into meters (m)
    dist_conv = {
        "m": 1.0,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "ft": 0.3048
    }

    # Converting values to SI units
    m1 = arr_val[0] * mass_conv[arr_unit[0]]
    m2 = arr_val[1] * mass_conv[arr_unit[1]]
    r = arr_val[2] * dist_conv[arr_unit[2]]

    # Calculate and return the gravitational force in Newtons
    return G * m1 * m2 / (r ** 2)


assert_approx_equals(solution([1000, 1000, 100], ["g", "kg", "m"]), 6.67e-12)
assert_approx_equals(solution([1000, 1000, 100], ["kg", "kg", "m"]), 6.6699999999999995e-09)
assert_approx_equals(solution([1000, 1000, 100], ["kg", "kg", "cm"]), 0.0000667)
