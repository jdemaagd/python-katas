# Introduction to Algorithm Design

## Introducing algorithms

- Essential for computer science and engineering
- Important other domains (computational biology, economics, ecology, communications, ecology, physics, etc.)
- They play a role in technology innovation
- They improve problem-solving and analytical thinking
- Characteristics
    - should be as specific as possible
    - should have each instruction properly defined
    - should not be any ambiguous instructions
    - all instructions of algorithm should be executable in a finite amount of time and in a finite number of steps
    - should have clear input and output to solve the problem
    - each instruction of algorithm should be integral in solving given problem
- Requirements
    - algorithm should be correct and should produce results as expected for all valid input values
    - algorithm should be optimal in sense that it should be executed on computer within desired time limit, in line
      with an optimal memory space requirement

## Performance analysis of an algorithm

- Time complexity
- Space complexity

## Asymptotic notation

- θ notation: denotes worst-case running time complexity with a tight bound
- Ο notation: denotes worst-case running time complexity with an upper bound, which ensures that function never grows
  faster than upper bound
- Ω notation: denotes lower bound of an algorithm’s running time, measures best amount of time to execute algorithm

## Amortized analysis

- Average performance of each operation in worst case considering cost of complete sequence of all operations. Amortized
  analysis is different from average-case analysis since distribution of input values is not considered. An amortized
  analysis gives average performance of each operation in worst case.
- Common Methods
    - Aggregate analysis: amortized cost is average cost of all sequences of operations; for a given sequence of n
      operations, amortized cost of each operation can be computed by dividing upper bound on total cost of n operations
      with
    - The accounting method: assign an amortized cost to each operation, which may be different than their actual cost;
      in this, we impose an extra charge on early operations in sequence and save `credit cost`, which is used to pay
      expensive operations later in sequence
    - The potential method: like accounting method, determine amortized cost of each operation and impose an extra
      charge to early operations that may be used later in sequence; unlike accounting method, potential method
      accumulates overcharged credit as `potential energy` of data structure as a whole instead of storing credit for
      individual operations

## Choosing complexity classes

## Computing the running time complexity of an algorithm
