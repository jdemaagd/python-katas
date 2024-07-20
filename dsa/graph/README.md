# Graphs

## BFS: Breadth First Search (Adjacency List)

- Visit neighbor nodes before visiting child nodes.
- Implementation is similar to BFS in case of binary tree.
- Queue: used to store nodes to be visited
    - neighbors are added to queue before child nodes
- Visited: used to keep track of visited nodes
    - to avoid revisiting nodes
- Output: how nodes are visited in level order traversal

## BFS: Time/Space Complexity Analysis

- T = O(V + E), where V is number of vertices and E is number of edges
    - we traverse every node once (vertex)
        - while loop as long as queue is not empty
    - we run for loop to add neighbors to queue
        - for loop runs for every edge
- S = O(V), where V is number of vertices
    - visited nodes
    - output visited nodes in level order
    - queue for enqueuing neighbor nodes
