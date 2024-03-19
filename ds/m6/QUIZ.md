# Exercises

## Question 1

```
Which of the following is a true about binary trees:
a. Every binary tree is either complete or full
b. Every complete binary tree is also a full binary tree
c. Every full binary tree is also a complete binary tree
d. No binary tree is both complete and full
e. None of the above

Solution
Option A is incorrect since it is not compulsory that a binary tree should be complete or full.
Option B is incorrect since a complete binary tree can have some nodes that are not filled in the
         last level, so a complete binary tree will not always be a full binary tree.
Option C is incorrect, as it is not always true, the following figure is a full binary tree, 
         but not a complete binary tree
Option D is incorrect, as it is not always true. 
         The following tree is both a complete and full binary tree       
```

## Question 2

```
Which of the tree traversal algorithms visit the root node last?

Solution
postorder traversal.
Using postorder traversal, we first visit the left subtree, 
then the right subtree, and finally we visit the root node.
```

## Question 3

```
Suppose we remove the root node 8, and we wish to replace it with any node from the left subtree, 
then what will be the new root?

Solution
The new node will be node 6. To maintain the properties of the binary search tree, 
the maximum value from the left subtree should be the new root.
```

## Question 4

```
What will be the inorder, postorder and preorder traversal of the following tree?

Solution
The preorder traversal will be 7-5-1-6-8-9
The inorder traversal will be 1-5-6-7-8-9
The postorder traversal will be 1-6-5-9-8-7
```

## Question 5

```
How do you find out if two trees are identical?

Solution
In order to find out if two binary trees are identical or not, both of the trees should have exactly
the same data and element arrangement. This can be done by traversing both of the trees with any
of the traversal algorithms (it should be the same for both trees) and matching them element by
element. If all the elements are the same in traversing both of the trees, then the trees are identical.
```

## Question 6

```
How many leaves are there in the tree mentioned in question number 4?

Solution
Three, nodes 1, 6, and 9
```

## Question 7

```
What is the relation between a perfect binary tree’s height and the number of nodes in that tree?

Solution
log2 (n+1) = h -> 2 is base 2
The number of nodes in each level:
    Level 0: 2^0 = 1 nodes
    Level 1: 2^1 = 2 nodes
    Level 2: 2^2 = 4 nodes
    Level 3: 2^3 = 8 nodes
The total nodes at level h can be computed by adding all nodes in each level:
    n = 2^0 + 2^1 + 2^2 + 2^3 + ... 2^(h-1) = 2^h - 1
So, the relationship between n and h is: n = 2^h - 1
    = log (n+1) = log2^h
    = log base 2 (n + 1) = h
```
