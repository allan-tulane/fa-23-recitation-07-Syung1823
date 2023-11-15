# CMPS 2200 Recitation 10## Answers

**Name:**__Simon Yung___
**Name:**___Killian Daly_


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work of Reachable will be $O(n*m)$

- **4)**
We only need to call reachable once since if the graph is connected all nodes are reachable and len of both the orignal graph and results will be the same
- **5)**
The work is the same as Reachable since you are calling it once $O(m*n)$
- **7)**
Yes the work will change: in the case of the adjacency matrix we can check for neigbors in constant time instead of using a iterator. Because of this the work will be $O(m+n)$
