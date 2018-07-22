The time and space complexity of common algorithms and data-structures
======

- Inspired by [Big-O Algorithm Complexity Cheat Sheet @ericdrowell](http://bigocheatsheet.com)
- For the complexity representation
  - 1 param: $\Theta(avg.)$
  - 2 params: $\Theta(avg.)$ / $O(worst)$
  - 3 params: $\Omega(best)$ / $\Theta(avg.)$ / $O(worst)$

## Data Structures

| Name | 结构名 | Space | Access | Search | Insert | Delete | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Array](http://en.wikipedia.org/wiki/Array_data_structure) | 数组 | $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | Swap with `a[-1]` => $O(1)$ in insert, delete |
| [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) | 队列 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) | 栈 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure)) | 堆 | | | | | | Check it in [Heap](./#heap) Section |
| [Graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) | 图 | | | | | | Check it in [Graph](./#graph) Section |
| [Singly-Linked List](https://en.wikipedia.org/wiki/Linked_list#Singly_linked_lists) | 单向链表 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| [Doubly-Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list) | 双向链表 | $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(n)$ / $O(n)$ | $\Theta(1)$ / $O(1)$ | $\Theta(1)$ / $O(1)$ | |
| [Skip List](https://en.wikipedia.org/wiki/Skip_list) | 跳跃表 | $O(n\log{n})$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| [Hash Table](https://en.wikipedia.org/wiki/Hash_table) | 哈希表 | $O(n)$ | - | $\Theta(1)$ / $O(n)$ | $\Theta(1)$ / $O(n)$ | $\Theta(1)$ / $O(n)$ | |
| [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree) | 二叉查找树 | $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| [Cartesian Tree](https://en.wikipedia.org/wiki/Cartesian_tree) | 笛卡尔树 | $O(n)$ | - | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |
| [B-Tree](https://en.wikipedia.org/wiki/B-tree) | B 树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| [Red-Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) | 红黑树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| [Splay Tree](https://en.wikipedia.org/wiki/Splay_tree) | 伸展树 | $O(n)$ | - | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree) | AVL 树 | $O(n)$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | $\Theta(\log{n})$ / $O(\log{n})$ | |
| [KD Tree](https://en.wikipedia.org/wiki/K-d_tree) | K 维树 | $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | $\Theta(\log{n})$ / $O(n)$ | |

### Heap

| Implementation | 结构名 | Heapify | Access Top | Pop Top | Increase Key | Insert | Delete | Merge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Linked List (Sorted) | 链表（已排序） | - | $\Theta(1)$ | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ | $\Theta(1)$ | $\Theta(m+n)$ |
| Linked List (Unsorted) | 链表（未排序） | - | $\Theta(n)$ | $\Theta(n)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ |
| [Binary Heap](https://en.wikipedia.org/wiki/Binary_heap) | 二叉堆 | $O(n)$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(m+n)$ |
| [Binomial Heap](https://en.wikipedia.org/wiki/Binomial_heap) | 二项堆 | - | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(\log{n})$ |
| [Fibonacci Heap](https://en.wikipedia.org/wiki/Fibonacci_heap) | 斐波那契堆 | - | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\log{n})$ | $\Theta(1)$ |

### Graph

- Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges

| Vertex / Edge Management | 结构名 | Storage | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Search |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Adjacency List](http://reference.wolfram.com/language/ref/AdjacencyList.html) | 邻接表 | $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert)$ |
| [Incidence List](http://reference.wolfram.com/language/ref/IncidenceList.html) | 关联表 | $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ |
| [Adjacency Matrix](http://reference.wolfram.com/language/ref/AdjacencyMatrix.html) | 邻接矩阵 | $O(\lvert{V}\rvert^2)$ | $\Theta(\lvert{V}\rvert^2)$ | $\Theta(1)$ | $\Theta(\lvert{V}\rvert^2)$ | $\Theta(1)$ | $\Theta(1)$ |
| [Incidence Matrix](http://reference.wolfram.com/language/ref/IncidenceMatrix.html) | 关联矩阵 | $O(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | $\Theta(\lvert{E}\rvert)$ |

## Algorithms

### Sorting Algorithms

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| [Quick Sort](https://en.wikipedia.org/wiki/Quicksort) | 快速排序 | $O(\log{n})$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n^2)$ | Basic<br />Unstable |
| [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort) | 归并排序 | $O(n)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Basic<br />Stable |
| [Heap Sort](https://en.wikipedia.org/wiki/Heapsort) | 堆排序 | $O(1)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Basic<br />Unstable |
| [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort) | 冒泡排序 | $O(1)$ | $\Omega(n)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| [Radix Sort](https://en.wikipedia.org/wiki/Radix_sort) | 基数排序 | $O(n+k)$ | $\Omega(nk)$ / $\Theta(nk)$ / $O(nk)$ | Basic<br />Stable |
| [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort) | 选择排序 | $O(1)$ | $\Omega(n^2)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Unstable |
| [Shell Sort](https://en.wikipedia.org/wiki/Shellsort) | 希尔排序 | $O(1)$ | $\Omega(n\log{n})$ / $\Theta(n(\log{n})^2)$ / $O(n(\log{n})^2)$ | Basic<br />Unstable |
| [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort) | 插入排序 | $O(1)$ | $\Omega(n)$ / $\Theta(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| [Tim Sort](https://en.wikipedia.org/wiki/Timsort) | 提姆排序 | $O(n)$ | $\Omega(n)$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Stable |
| [Bucket Sort](https://en.wikipedia.org/wiki/Bucket_sort) | 桶排序 | $O(n)$ | $\Omega(n+k)$ / $\Theta(n+k)$ / $O(n^2)$ | Stable |
| [Tree Sort](https://en.wikipedia.org/wiki/Tree_sort) | 树排序 | $O(n)$ | $\Omega(n\log{n})$ / $\Theta(n\log{n})$ / $O(n^2)$ | |
| [Counting Sort](https://en.wikipedia.org/wiki/Counting_sort) | 计数排序 | $O(k)$ | $\Omega(n+k)$ / $\Theta(n+k)$ / $O(n+k)$ | Stable |
| [Cube Sort](https://en.wikipedia.org/wiki/Cubesort) | 立方排序 | $O(n)$ | $\Omega(n)$ / $\Theta(n\log{n})$ / $O(n\log{n})$ | Stable |

### Searching Algorithms

- Graph with $\lvert{V}\rvert$ vertices and $\lvert{E}\rvert$ edges

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search) | 深度优先搜索 | $O(\lvert{V}\rvert)$ | - / $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | |
| [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search) | 广度优先搜索 | $O(\lvert{V}\rvert)$ | - / $O(\lvert{V}\rvert+\lvert{E}\rvert)$ | |
| [Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm) | 二分搜索 | $O(1)$ | $\Theta(\log{n})$ / $O(\log{n})$ | Sorted array of n elements |
| [Brute Force](https://en.wikipedia.org/wiki/Brute-force_search) | 穷举搜索 | $O(1)$ | $\Theta(n)$ / $O(n)$ | Array |
| [Shortest path by Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) | | $O(\lvert{V}\rvert)$ | $\Theta(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ / $O(\lvert{V}\rvert\cdot\lvert{E}\rvert)$ | |
| [Shortest path by Dijkstra (Min-heap)](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) | | $O(\lvert{V}\rvert)$ | $\Theta((\lvert{V}\rvert+\lvert{E}\rvert)\cdot\log{\lvert{V}\rvert})$ / $O((\lvert{V}\rvert+\lvert{E}\rvert)\cdot\log{\lvert{V}\rvert})$ | |
| Shortest path by Dijkstra (Unordered Array) | | $O(\lvert{V}\rvert)$ | $\Theta(\lvert{V}\rvert^2)$ / $O(\lvert{V}\rvert^2)$ | |
