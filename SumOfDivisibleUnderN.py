def SumOfDivisibleUnderN(divisor: int, N: int):
    """Returns the sum of all numbers divisible by the divisor up to but not including N"""
    start = FindStart(divisor, 0)
    stop = FindStop(divisor, N-1)
    res = ArithmeticSum(start, stop, divisor)
    return res

def FindStart(divisor: int, lowerBound: int):
    """Helper function for arithmetic sum. Finds the starting term in the sequence"""
    if lowerBound == 0:
        lowerBound = 1
    res = lowerBound
    while res%divisor != 0:
        res += 1
    return res

def FindStop(divisor: int, upperBound: int):
    """Helper function for arithmetic sum. Finds the final term in the sequence"""
    res = upperBound
    while res%divisor != 0:
        res -= 1
    return res

def ArithmeticSum(start: int, stop: int, step: int):
    """Uses the arithmetic formula (widely attributed to Gauss) to find the sum of a sequence giving a starting point, a stopping point, and a step"""
    numSteps = (stop - start)//step + 1
    return (numSteps * (stop + start))/2

total = SumOfDivisibleUnderN(5,1000) + SumOfDivisibleUnderN(3,1000) - SumOfDivisibleUnderN(15, 1000)

print(total)