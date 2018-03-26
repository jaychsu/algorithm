The time and space complexity of common algorithms and data-structures
======

* Sourced from [Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell](http://bigocheatsheet.com/)
* For the complexity representation
  * 1 param: $\Theta(avg.)$
  * 2 paras: $\Theta(avg.)$ / $O(worst)$
  * 3 paras: $\Omega(best)$ / $\Theta(avg.)$ / $O(worst)$

## Data Structures

| Name | 结构名 | Space | Access | Search | Insert | Delete | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Array | 数组 | $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | Swap with `a[-1]` => $O(1)$ in insert, delete |
| Queue | 队列 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| Stack | 栈 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| Heap | 堆 | | | | | | Check it in [Heap](./#heap) Section |
| Graph | 图 | | | | | | Check it in [Graph](./#graph) Section |
| Singly-Linked List | 单向链表 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| Doubly-Linked List | 双向链表 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| Skip List | 跳跃表 | $O(n\log{n})$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| Hash Table | 哈希表 | $O(n)$ | - | $\Theta(1)$ / $O(n)$ | $\Theta(1)$ / $O(n)$ | $\Theta(1)$ / $O(n)$ | |
| Binary Search Tree | 二叉查找树 | $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| Cartesian Tree | 笛卡尔树 | $O(n)$ | - | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| B-Tree | B 树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| Red-Black Tree | 红黑树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| Splay Tree | 伸展树 | $O(n)$ | - | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| AVL Tree | AVL 树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| KD Tree | K 维树 | $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |

### Heap

| Implementation | 结构名 | Heapify | Access Top | Pop Top | Increase Key | Insert | Delete | Merge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Linked List (Sorted) | 链表（已排序） | - | $\Theta(1)$ | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ | $\Theta(1)$ | $\Theta(m+n)$ |
| Linked List (Unsorted) | 链表（未排序） | - | $\Theta(n)$ | $\Theta(n)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ |
| Binary Heap | 二叉堆 | $O(n)$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(m+n)$ |
| Binomial Heap | 二项堆 | - | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ |
| Fibonacci Heap | 斐波那契堆 | - | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(1)$ |

### Graph

| Vertex / Edge Management | 结构名 | Storage | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Search |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Adjacency List | 邻接表 | $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert)$ |
| Incidence List | 关联表 | $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ |
| Adjacency Matrix | 邻接矩阵 | $O(\lvert{V}\rvert^2)$ | $\Theta(\lvert{V}\rvert^2)$ | $\Theta(1)$ | $\Theta(\lvert{V}\rvert^2)$ | $\Theta(1)$ | $\Theta(1)$ |
| Incidence Matrix | 关联矩阵 | $O(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ |

## Algorithms

### Sorting Algorithms

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| Quick Sort | 快速排序 | $O(\log{n})$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n^2)$ | Basic<br />Unstable |
| Merge Sort | 归并排序 | $O(n)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Basic<br />Stable |
| Heap Sort | 堆排序 | $O(1)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Basic<br />Unstable |
| Bubble Sort | 冒泡排序 | $O(1)$ | $\Omega(n)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| Radix Sort | 基数排序 | $O(n+k)$ | $\Omega(nk)$ / $\Theta(nk)$ / $O(nk)$ | Basic<br />Stable |
| Selection Sort | 选择排序 | $O(1)$ | $\Omega(n^2)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Unstable |
| Shell Sort | 希尔排序 | $O(1)$ | $\Omega(n\log{n})$ / $\Theta(n(\log{n})^2)$ / $O(n(\log{n})^2)$ | Basic<br />Unstable |
| Insertion Sort | 插入排序 | $O(1)$ | $\Omega(n)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| Tim Sort | Tim 排序 | $O(n)$ | $\Omega(n)$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Stable |
| Bucket Sort | 桶排序 | $O(n)$ | $\Omega(n+k)$ / $\Theta(n+k)$ / $O(n^2)$ | Stable |
| Tree Sort | 树排序 | $O(n)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n^2)$ | |
| Counting Sort | 计数排序 | $O(k)$ | $\Omega(n+k)$ / $\Theta(n+k)$ / $O(n+k)$ | Stable |
| Cube Sort | | $O(n)$ | $\Omega(n)$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Stable |

### Searching Algorithms

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| Depth First Search | 深度优先搜索 | $O(\lvert{V}\rvert)$ | - / $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges |
| Breadth First Search | 广度优先搜索 | $O(\lvert{V}\rvert)$ | - / $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges |
| Binary Search | 二分搜索 | $O(1)$ | $\Theta(\log{n})$ / $O(\log{n})$ | Sorted array of n elements |
| Brute Force | 穷举搜索 | $O(1)$ | $\Theta(n)$ / $O(n)$ | Array |
| Shortest path by Bellman-Ford | | $O(\lvert{V}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ / $O(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges |
| Shortest path by Dijkstra (Min Heap) | | $O(\lvert{V}\rvert)$ | $\Theta((\lvert{V}\rvert+\lvert{E}\rvert)\cdot\log{\lvert{V}\rvert})$ / $O((\lvert{V}\rvert+\lvert{E}\rvert)\cdot\log{\lvert{V}\rvert})$ | Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges |
| Shortest path by Dijkstra (Unordered Array) | | $O(\lvert{V}\rvert)$ | $\Theta(\lvert{V}\rvert^2)$ / $O(\lvert{V}\rvert^2)$ | Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges |
