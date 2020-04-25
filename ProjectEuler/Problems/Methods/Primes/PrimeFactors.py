from math import ceil, sqrt
from .PrimeSieve import PrimeSieve

def PrimeFactors(n: int):
    """"Finds the prime factors of an integer n"""
    primeFactors = []
    #A number n cannot have a prime factor larger than sqrt n.
    ceiling = ceil(sqrt(n))
    factorCandidates = PrimeSieve(ceiling)

    while(n > 1):
        for i in range(0, len(factorCandidates)):
            if(n%factorCandidates[i] == 0):
                n=n/factorCandidates[i]
                primeFactors.append(factorCandidates[i])
                break
    return primeFactors
     