from math import sqrt

rt5 = sqrt(5)

phi = (1 + rt5)/2

def GenerateNthFibonacci(n: int):
    """Solving the 2nd order linear differential equation F_n = F_n-1 + F_n-2 with F_0 = 0 F_1 = 1
    we can generate the nth term of the Fibonacci sequence"""
    return phi**n/rt5  -  (1-phi)**n/rt5