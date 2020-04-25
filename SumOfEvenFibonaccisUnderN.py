from math import sqrt

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


rt5 = sqrt(5)

phi = (1 + rt5)/2

def GenerateNthFibonacci(n: int):
    """Solving the 2nd order linear differential equation F_n = F_n-1 + F_n-2 with F_0 = 0 F_1 = 1
    we can generate the nth term of the Fibonacci sequence"""
    return phi**n/rt5  -  (1-phi)**n/rt5

res = SumOfEvenFibonaccisUnderN(4000000)

print(res)