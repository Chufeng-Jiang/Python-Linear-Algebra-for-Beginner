# 包中的变量，但是对包外不可见，因此使用“_”开头
EPSILON = 1e-8


def is_zero(x):
    return abs(x) < EPSILON


def is_equal(a, b):
    return abs(a - b) < EPSILON