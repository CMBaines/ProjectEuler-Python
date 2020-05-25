from .ArithmeticSum import ArithmeticSum

def SumOfDivisibleUnderN(divisor: int, n: int):
    """Returns the sum of all numbers divisible by the divisor up to but not including n"""
    res = ArithmeticSum(n, divisor)
    return res