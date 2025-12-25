def solve(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return solve(W, wt, val, n-1)
    else:
        return max(val[n-1] + solve(W - wt[n-1], wt, val, n-1), solve(W, wt, val, n-1))

# Test Data
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print("Naive Result:", solve(W, wt, val, len(val)))
