# Exercises

## Question 1

```
On average, how many comparisons are required in a linear search of n elements?

Solution 
When a search element is found at the 1st position, 2nd position, 3rd position, 
and similarly at the nth position, correspondingly,
it will require 1, 2, 3... n number of comparisons.
Therefore, the average number of comparisons required in a linear search of n elements is 
(1 + 2 + 3 + ... + n) / n = (n + 1) / 2
```

## Question 2

```
Assume there are eight elements in a sorted array.
What is average number of comparisons that will be required if all searches are successful 
and if the binary search algorithm is used?

Solution
Average number of comparisons = (1 + 2 + 2 + 3 + 3 + 3 + 3 + 4) / 8 = 21/8
```

## Question 3

```
What is worst-case time complexity of binary search algorithm?

Solution
In that case, log(n) comparisons will be required -> O(log n)
```

## Question 4

```
When should interpolation search algorithm perform better than binary search algorithm?

Solution
When data items in the array are uniformly distributed
```
