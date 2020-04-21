def SumOfDivisibleUnderN(divisor: int, N: int):
    start = FindStart(divisor, 0)
    stop = FindStop(divisor, N-1)
    res = ArithmeticSum(start, stop, divisor)
    return res

def FindStart(divisor: int, lowerBound: int):
    if lowerBound == 0:
        lowerBound = 1
    res = lowerBound
    while res%divisor != 0:
        res += 1
    return res

def FindStop(divisor: int, upperBound: int):
    res = upperBound
    while res%divisor != 0:
        res -= 1
    return res

def ArithmeticSum(start: int, stop: int, step: int):
    numSteps = (stop - start)//step + 1
    return (numSteps * (stop + start))/2

total = SumOfDivisibleUnderN(5,1000) + SumOfDivisibleUnderN(3,1000) - SumOfDivisibleUnderN(15, 1000)

print(total)