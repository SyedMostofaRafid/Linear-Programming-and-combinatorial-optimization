import time
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def fibonacci_series(n):
    series = []
    for i in range(n + 1):
        series.append(fibonacci(i))
    return series
n = int(input("Enter the position of the Fibonacci number: "))
st= time.time() 
series = fibonacci_series(n)
et= time.time()
t=et-st
print(f"The Fibonacci series of {n} number is: {series}")
print(f"The {n}th Fibonacci number is: {series[-1]}")
print(t)