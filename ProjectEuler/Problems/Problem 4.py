#We assume that the largest palindrome will begin and end with 9.
#Therefore, the product candidates (m,n) for the largest palindrome must be of the following form:
#..9 x ..1, ..3 x ..3, or ..7 x ..7 and n, m > 900
#Additionally, a palindrom is of the form abc...cba
# = 10^5*a + 10^4*b + 10^3*c + 10^2*c + 10*b + a
# = (10^5+10^0)*a + (10^4*10^1)*b + (10^3 + 10^2)*c
#Odd powers of 10 = -1 mod 11, even powers of 10 = 1 mod 11
#Therefore each of these pairings = 0 mod 11
#n*m = 11*(9091*a+910*b+100*c)
#Therefore, n or m has a prime factor of 11, but not both
#So to sumarize:
#n != m
#n, m > 900
#n, m end in 1, 3, 7, or 9
#n = s*11 and m mod 11 != 0
#Therefore candidates for n are 913, 957, and 979
#If n = 979, candidates for m are 991, 981, ... , 901
#If n = 957, candidates for m are 997, 987, ... , 967, 947, ... , 907
#If n = 913, candidates for m are 993, 983, ... , 923, 903

from Methods.PalindromicNumbers.isPalindromic import isPalindromic

n = 979
m = 0
res = 0

for x in range(991, 900, -10):
    if(isPalindromic(n*x) and n*x > res):
        res = n*x
        m = x
        #We can add a break here as we know that 979*991 > 979*981 > ... > 979*901
        break

n = 957

for x in range(997, 906, -10):
    if(n != x and isPalindromic(n*x) and n*x > res):
        res = n*x
        m = x
        break

n = 913

for x in range(993, 902, -10):
    if(n != x and isPalindromic(n*x) and n*x > res):
        res = n*x
        m = x
        break

print(res, n, m)