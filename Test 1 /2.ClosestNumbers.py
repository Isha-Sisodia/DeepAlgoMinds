Question Link - https://www.hackerrank.com/challenges/closest-numbers/problem
def closestNumbers(a):
    n = len(a)
  
    a.sort()

    min_diff = float('inf')

    for i in range(n-1):
        diff = a[i+1] - a[i]
        min_diff = min(min_diff, diff)

    ans = []

    for i in range(n-1):
        diff = a[i+1] - a[i]

        if diff == min_diff:
            ans.append(a[i])
            ans.append(a[i+1])

    return ans
