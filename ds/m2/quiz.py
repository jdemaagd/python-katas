# NOTE: O(log(n)).
# As we are multiplying integer i by 2 in each step
# there will be exactly log(n) steps
# (1, 2, 4, ... till n)
i = 1
while (i < n):
    i *= 2
    print("data")

# NOTE: O(log(n))
# As we are dividing integer i by 2 in each step
# there will be exactly log(n) steps
# (n, n/2, n/4, ... till 1)
i = n
while (i > 0):
    print('complexity')
    i /= 2

# NOTE: outer loop will run n times for each i in outer loop,
# while inner while loop will run log(i) times because we are multiplying
# each of j values by 2 until it is less than n
# hence, there will be a maximum of log(n) steps in the inner loop
# so, overall complexity will be O(nlog(n))
for i in range(1, n):
    j = i
    while (j < n):
        j *= 2

# NOTE: while loop will execute based on value of i until condition becomes false
# value of i is incrementing in following series:
# 2, 4, 16, 256, ... n
# we can see that number of times loop is executing is log2(log2(n)) for a given value of n
# so, for this series there will be exactly log2(log2(n)) executions of the loop
# hence time complexity will be O(log2(log2(n))  -> 2s are base 2
i = 1
while (i < n):
    print('python')
    i = i ** 2
