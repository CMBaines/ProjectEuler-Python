from math import sqrt

def SumOfEvenFibonaccisUnderN(N: int):
    sum = 0
    m = 3
    while True:
        term = GenerateNthFibonacci(m)
        if term >= N:
            return sum
        sum += term
        m += 3


def GenerateNthFibonacci(n: int):
    return (((1+sqrt(5))/2)**n)/sqrt(5)  -  ((1-((1+sqrt(5))/2))**n)/sqrt(5)

res = SumOfEvenFibonaccisUnderN(4000000)

print(res)