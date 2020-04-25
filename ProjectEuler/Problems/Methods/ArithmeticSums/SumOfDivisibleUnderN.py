from .ArithmeticSum import ArithmeticSum

def SumOfDivisibleUnderN(divisor: int, N: int):
    """Returns the sum of all numbers divisible by the divisor up to but not including N"""
    res = ArithmeticSum(N, divisor)
    return res