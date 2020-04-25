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

def ArithmeticSum(upperBound: int, step: int, lowerBound: int=0):
    """Uses the arithmetic formula (widely attributed to Gauss) to find the sum of a sequence giving a starting point, a stopping point, and a step"""
    start = FindStart(step, lowerBound)
    stop = FindStop(step, upperBound)
    numSteps = (stop - start)//step + 1
    return (numSteps * (stop + start))/2