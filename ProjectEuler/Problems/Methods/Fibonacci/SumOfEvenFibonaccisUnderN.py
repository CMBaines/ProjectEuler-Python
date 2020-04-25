from .GenerateNthFibonacci import GenerateNthFibonacci

def SumOfEvenFibonaccisUnderN(N: int):
    """Using the fact that every third term of the Fibonacci sequence is even this returns the sum of the Fibonaccis under N
    without generating all the intermidiate odd Fibonacci numbers"""
    sum = 0
    m = 3
    while True:
        term = GenerateNthFibonacci(m)
        if term >= N:
            return sum
        sum += term
        m += 3