'''
Problem: Distinct Order Traversal

You are given an undirected, connected graph with g nodes, labeled 1 … g

M edges described by two arrays g_from and g_to, where the i-th edge connects g_from[i] and g_to[i].

Goal

Traversal Array A
Starting at any node you like, traverse the graph so that every node is visited at least once.
You may revisit nodes and edges any number of times.
Record the exact sequence of node visits as array A.

Distinct Array B
After you finish traversal, build a new array B using the following process:

B = []
for i in range(len(A)):
    found = False
    for j in range(len(B)):
        if A[i] == B[j]:
            found = True
            break
    if not found:
        B.append(A[i])


In other words, B is simply A with duplicates removed, keeping the first appearance order.

Objective
Choose a traversal order A so that the resulting array B is lexicographically largest (in dictionary order) among all possible valid traversals.

Return the final array B.
'''
from collections import defaultdict, deque

def distinctTraversalOrder (edges:list) -> list:
    adj_map = defaultdict(list)
    for i,j in edges:
        adj_map[i].append(j)
        adj_map[j].append(i)
    
    stack = deque()
    start = 0
    target = 1000000
    for i in adj_map:
        start = max(start, i)
        target = min(target, i)
    
    stack.appendleft(start)
    visited = set()
    traverse = []

    while stack:
        curr = stack.popleft()
        
        if curr in visited:
            continue
        visited.add(curr)
        traverse.append(curr)

        neighbors = adj_map[curr]
        neighbors.sort()

        for i in neighbors:
            stack.appendleft(i)
    
    return traverse

print(f"Result: {distinctTraversalOrder([(4,5), (5,1), (1,4), (4,3), (3,2)])}")
print("Expected [5,4,3,2,1]")

print(f"Result: {distinctTraversalOrder([[1,2],[2,3],[2,4]])}")
print("Expected [4,3,2,1]")

print(f"Result: {distinctTraversalOrder([[1,2],[2,3],[3,4],[4,1]])}")
print("Expected [4,3,2,1]")

print(f"Result: {distinctTraversalOrder([[1,2],[1,3],[2,4],[2,5],[3,5]])}")
print("Expected [5,4,3,2,1]")

print(f"Result: {distinctTraversalOrder([[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[3,5]])}")
print("Expected [6,5,4,3,2,1]")
