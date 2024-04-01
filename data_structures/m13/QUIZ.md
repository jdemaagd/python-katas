# Exercises

## Question 1

```
Show the KMP prefix function for the pattern "aabaabcab".
```
|   pattern   |  a  |  a  |  b  |  a  |  a  |  b  |  c  |  a  |  b  |
|:-----------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|   prefix    |  0  |  1  |  0  |  1  |  2  |  0  |  0  |  1  |  2  |
| function 𝜋 |  0  |  1  |  0  |  1  |  2  |  0  |  0  |  1  |  2  |

## Question 2

```
If the expected number of valid shifts is small and the modulus is larger than the length
of the pattern, then what is the matching time of the Rabin-Karp algorithm?

a. Theta (m)
b. Big O (n+m)
c. Theta (n-m)
d. Big O (n)

Solution: b. Big O (n+m)
```

## Question 3

```
How many spurious hits does the Rabin-Karp string matching algorithm encounter in the
text T = "3141512653849792" when looking for all occurrences of the pattern P = "26",
working modulo q = 11, and over the alphabet set Σ = {0, 1, 2,..., 9}?

Solution: 2
```

## Question 4

```
What is the basic formula applied in the Rabin-Karp algorithm 
to get the computation time as Theta (m)?
a. Halving rule
b. Horner's rule
c. Summation lemma
d. Cancellation lemma

Soltuinb: b. Horner's rule
```

## Question 5

```
The Rabin-Karp algorithm can be used for discovering plagiarism in text documents.
a. True
b. False

Solution: a. True
```
