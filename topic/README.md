The time and space complexity of common algorithms and data-structures
======

* Sourced from [Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell](http://bigocheatsheet.com/)
* For the complexity representation
  * 1 param: {avg.}
  * 2 paras: {avg.} / {worst}
  * 3 paras: {best} / {avg.} / {worst}

## Data Structures

| Name | 结构名 | Space | Access | Search | Insert | Delete | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Array | 数组 | $O(n)$ | $O(1)$ / $O(1)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | Swap with `a[-1]` => $O(1)$ in insert, delete |
| Queue | 队列 | $O(n)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(1)$ | |
| Stack | 栈 | $O(n)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(1)$ | |
| Heap | 堆 | Check it in [Heap](./#heap) Section | | | | | |
| Graph | 图 | Check it in [Graph](./#graph) Section | | | | | |
| Singly-Linked List | 单向链表 | $O(n)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(1)$ | |
| Doubly-Linked List | 双向链表 | $O(n)$ | $O(n)$ / $O(n)$ | $O(n)$ / $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(1)$ | |
| Skip List | 跳跃表 | $O(n\log{n})$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | |
| Hash Table | 哈希表 | $O(n)$ | - | $O(1)$ / $O(n)$ | $O(1)$ / $O(n)$ | $O(1)$ / $O(n)$ | |
| Binary Search Tree | 二叉查找树 | $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | |
| Cartesian Tree | 笛卡尔树 | $O(n)$ | - | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | |
| B-Tree | B 树 | $O(n)$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | |
| Red-Black Tree | 红黑树 | $O(n)$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | |
| Splay Tree | 伸展树 | $O(n)$ | - | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | |
| AVL Tree | AVL 树 | $O(n)$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | $O(\log{n})$ / $O(\log{n})$ | |
| KD Tree | K 维树 | $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | $O(\log{n})$ / $O(n)$ | |

### Heap

| Implementation | 中文 | Heapify | Access Top | Pop Top | Increase Key | Insert | Delete | Merge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Linked List (Sorted) | 链表（已排序） | - | $O(1)$ | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | $O(m+n)$ |
| Linked List (Unsorted) | 链表（未排序） | - | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| Binary Heap | 二叉堆 | $O(n)$ | $O(1)$ | $O(\log{n})$ | $O(\log{n})$ | $O(\log{n})$ | $O(\log{n})$ | $O(m+n)$ |
| Binomial Heap | 二项堆 | - | $O(1)$ | $O(\log{n})$ | $O(\log{n})$ | $O(1)$ | $O(\log{n})$ | $O(\log{n})$ |
| Fibonacci Heap | 斐波那契堆 | - | $O(1)$ | $O(\log{n})$ | $O(1)$ | $O(1)$ | $O(\log{n})$ | $O(1)$ |

### Graph

| Vertex / Edge Management | 中文 | Storage | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Search |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Adjacency List | 邻接表 | $O(\|V\|+\|E\|)$ | $O(1)$ | $O(1)$ | $O(\|V\|+\|E\|)$ | $O(\|E\|)$ | $O(\|V\|)$ |
| Incidence List | 关联表 | $O(\|V\|+\|E\|)$ | $O(1)$ | $O(1)$ | $O(\|E\|)$ | $O(\|E\|)$ | $O(\|E\|)$ |
| Adjacency Matrix | 邻接矩阵 | $O(\|V\|^2)$ | $O(\|V\|^2)$ | $O(1)$ | $O(\|V\|^2)$ | $O(1)$ | $O(1)$ |
| Incidence Matrix | 关联矩阵 | $O(\|V\|\cdot\|E\|)$ | $O(\|V\|\cdot\|E\|)$ | $O(\|V\|\cdot\|E\|)$ | $O(\|V\|\cdot\|E\|)$ | $O(\|V\|\cdot\|E\|)$ | $O(\|E\|)$ |

## Algorithms

### Sorting Algorithms

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| Quick Sort | 快速排序 | $O(\log{n})$ | $O(n\log{n})$ / $O(n\log{n})$ / $O(n^2)$ | Basic<br />Unstable |
| Merge Sort | 归并排序 | $O(n)$ | $O(n\log{n})$ / $O(n\log{n})$ / $O(n\log{n})$ | Basic<br />Stable |
| Heap Sort | 堆排序 | $O(1)$ | $O(n\log{n})$ / $O(n\log{n})$ / $O(n\log{n})$ | Basic<br />Unstable |
| Bubble Sort | 冒泡排序 | $O(1)$ | $O(n)$ / $O(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| Radix Sort | 基数排序 | $O(n+k)$ | $O(nk)$ / $O(nk)$ / $O(nk)$ | Basic<br />Stable |
| Selection Sort | 选择排序 | $O(1)$ | $O(n^2)$ / $O(n^2)$ / $O(n^2)$ | Basic<br />Unstable |
| Shell Sort | 希尔排序 | $O(1)$ | $O(n\log{n})$ / $O(n(\log{n})^2)$ / $O(n(\log{n})^2)$ | Basic<br />Unstable |
| Insertion Sort | 插入排序 | $O(1)$ | $O(n)$ / $O(n^2)$ / $O(n^2)$ | Basic<br />Stable |
| Tim Sort | Tim 排序 | $O(n)$ | $O(n)$ / $O(n\log{n})$ / $O(n\log{n})$ | Stable |
| Bucket Sort | 桶排序 | $O(n)$ | $O(n+k)$ / $O(n+k)$ / $O(n^2)$ | Stable |
| Tree Sort | 树排序 | $O(n)$ | $O(n\log{n})$ / $O(n\log{n})$ / $O(n^2)$ | |
| Counting Sort | 计数排序 | $O(k)$ | $O(n+k)$ / $O(n+k)$ / $O(n+k)$ | Stable |
| Cube Sort | | $O(n)$ | $O(n)$ / $O(n\log{n})$ / $O(n\log{n})$ | Stable |

### Searching Algorithms

| Name | 算法名 | Space | Time | Note |
| --- | --- | --- | --- | --- |
| Depth First Search | 深度优先搜索 | $O(\|V\|)$ | - / $O(\|V\|+\|E\|)$ | Graph of \|V\|vertices and \|E\|edges |
| Breadth First Search | 广度优先搜索 | $O(\|V\|)$ | - / $O(\|V\|+\|E\|)$ | Graph of \|V\|vertices and \|E\|edges |
| Binary Search | 二分搜索 | $O(1)$ | $O(\log{n})$ / $O(\log{n})$ | Sorted array of n elements |
| Brute Force | 暴风算法 | $O(1)$ | $O(n)$ / $O(n)$ | Array |
| Shortest path by Bellman-Ford | | $O(\|V\|)$ | $O(\|V\|\cdot\|E\|)$ / $O(\|V\|\cdot\|E\|)$ | Graph of \|V\|vertices and \|E\|edges |
| Shortest path by Dijkstra | | | | Graph of \|V\|vertices and \|E\|edges |
