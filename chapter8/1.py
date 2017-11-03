# Write a method to generate the nth Fibonacci number

# Compute Fibonacci using recursion and memoization
#   memoization used to improve average time
# Params: n(compute nth fib number)
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def fibRecursive(n, oracle):
    assert n > 0
    if n==1:
        return 0
    if n==2:
        return 1
    if oracle.has_key(n-1):
        n_prime = oracle[n-1]
    else:
        n_prime = fibRecursive(n-1, oracle)
        oracle[n-1]=n_prime
    if oracle.has_key(n-2):
        n_dprime = oracle[n-2]
    else:
        n_dprime = fibRecursive(n-2, oracle)
        oracle[n-2] = n_dprime
    return n_prime + n_dprime

# Compute Fibonacci using looping
# Params: n(compute nth fib number)
# Time Complexity: O(n)
# Space Complexity: O(n)
def fibLoop(n):
    assert n > 0
    if n==1:
        return 0
    if n==2:
        return 1
    A=[0]*n
    A[1]=1
    for i in range(2,n):
        A[i] = A[i-1] + A[i-2]
    return A[n-1]

def testBench():
    tn = [1,2,3,10,23,50]
    texpected = [0,1,1,34,17711,7778742049]
    oracle = dict()
    
    for x in range(len(tn)):
        ret=fibRecursive(tn[x],oracle)
        assert ret == texpected[x], "Input: " + str(tn[x]) + " Got " + str(ret) + " Expected " + str(texpected[x])
        ret=fibLoop(tn[x])
        assert ret == texpected[x], "Input: " + str(tn[x]) + " Got " + str(ret) + " Expected " + str(texpected[x])

if __name__=="__main__":testBench()
