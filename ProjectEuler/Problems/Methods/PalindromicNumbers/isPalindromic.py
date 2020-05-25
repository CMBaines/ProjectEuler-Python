def isPalindromic(n: int):
    """Determines if a number is palindromic (reads the same forwards and backwards)"""
    return str(n) == str(n)[::-1]