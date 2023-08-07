# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
Input*: 3
Output*: "3"
"""

n = 5

def distinct_ways(n) :
    if n<=1 :
        return 1
    else :
        count = distinct_ways(n-1) + distinct_ways(n-2)
        return count


result = distinct_ways(n)
print(result)
