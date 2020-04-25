from math import sqrt

def PrimeSieve(lim: int):
    """Find a list of primes less than a given limit"""
    #TODO, add db storage of known primes
    primeCandidates = list(range(2,lim+1))

    i=0
    while(primeCandidates[i] <= sqrt(lim)):
        primeCandidates = [j for j in primeCandidates if (j == primeCandidates[i] or j%primeCandidates[i] != 0)]
        i += 1
    
    return primeCandidates
