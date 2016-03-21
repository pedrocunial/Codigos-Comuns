def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    ret = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = ret
    return ret

print(fib_memo(6))
