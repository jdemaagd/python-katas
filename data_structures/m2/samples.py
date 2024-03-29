# NOTE: T(n) = constant time (c) * n = c*n = O(n)
for i in range(n):
    print("data") #constant time

# NOTE: O(n^2) print statement will be executed n2 times,
# n times for the inner loop, and,
# for each iteration of the outer loop, the inner loop will be executed
for i in range(n):
    for j in range(n): # This loop will also run for n times
        print("run")

# NOTE: O(n) since print statement will run n times
# because inner loop executes only once due to a break statement
for i in range(n):
    for j in range(n):
        print("run fun")
        break

# NOTE: print statements will execute n times in the first loop
# and n^2 times for the second nested loop
# T(n) = constant time (c1) * n + c2*n*n = O(n^2)
def fun(n):
    for i in range(n):
        print("data") #constant time
    #outer loop execute for n times
    for i in range(n):
        for j in range(n): #inner loop execute n times
            print("run fun") #constant time

# NOTE: worst-case runtime complexity will be time required
# for execution of all statements; that is, time required
# for execution of if-else conditions, and for loop
# T(n) = c1 + c2 n = O(n)
if n == 0: #constant time
    print("data")
else:
    for i in range(n): #loop run for n times
        print("structure")

# NOTE: loop will terminate based on value of i
#       loop will iterate :based on condition: i^2 <= n
# T(n) = O(sqrt(n))
i = 1
j = 0
while i*i < n:
    j = j +1
    i = i+1
    print("data")

# NOTE: outer loop executes n/2 times
#       middle loop will also run n/2 times
#       innermost loop will run for log(n) time
# Total running time: O(n*n*logn)
i = 0
for i in range(int(n / 2), n):
    j = 1
    while j + n / 2 <= n:
        k = 1
        while k < n:
            k *= 2
            print("data")
            j += 1
