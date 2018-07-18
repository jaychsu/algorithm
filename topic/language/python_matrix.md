Matrix Iteration
======

## To convert the 2D matrix to the 1D list

```python
# For any m * n matrix
# 0 <= x < m, 0 <= y < n
# The cell at `[i, j]` can be mapped to `k` in list
k = i * n + j
```

## To iterate around the current cell

means to visit the cell at the top/bottom/left/right

```python
VECTOR = (
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
)

x, y = 1, 1
for dx, dy in VECTOR:
    print(x + dx, y + dy)

# 0, l: (0, 1)
# 1, r: (2, 1)
# 2, t: (1, 0)
# 3, b: (1, 2)
```

## To avoid returning along the original path, just simply set the last visited cell to `'#'`

see [lintcode/132_word_search_ii.py](../lintcode/132_word_search_ii.py)

## Traverse the half triangle in matrix

```python
>>> n = 4
>>> arr = [[0] * n for _ in range(n)]
>>> arr
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]

>>> for x in range(n - 1, -1, -1):
...     for y in range(x, n):
...             arr[x][y] = 1
>>> arr
[[1, 1, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 1, 1],
 [0, 0, 0, 1]]

>>> for y in range(n - 1, -1, -1):
...     for x in range(y, n):
...             arr[x][y] = 2
>>> arr
[[2, 1, 1, 1],
 [2, 2, 1, 1],
 [2, 2, 2, 1],
 [2, 2, 2, 2]]

>>> frozen_line = 2
>>> for y in range(n - 1 - frozen_line, -1, -1):
...     for x in range(y + frozen_line, n):
...             arr[x][y] = 3
>>> arr
[[2, 1, 1, 1],
 [2, 2, 1, 1],
 [3, 2, 2, 1],
 [3, 3, 2, 2]]
```

### Need to init status by recursing from diagonal line

since sometimes we need to init status from bottom-left cell, see [lintcode/136_palindrome_partitioning.py](../lintcode/136_palindrome_partitioning.py)

```python
>>> n = 5
>>> level = order = 0
>>> arr = [[0] * n for _ in range(n)]
>>> for y in range(n):
...     order += 1
...     arr[y][y] = order
...     if y > 0:
...             x = y - 1
...             arr[x][y] = order
>>> arr
[[1, 2, 0, 0, 0],
 [0, 2, 3, 0, 0],
 [0, 0, 3, 4, 0],
 [0, 0, 0, 4, 5],
 [0, 0, 0, 0, 5]]

>>> level = order = 0
>>> for x in range(n - 1 - 2, -1, -1):
...     level += 10
...     order = 0
...     for y in range(x + 2, n):
...             order += 1
...             arr[x][y] = level + order
>>> arr
[[ 1,  2, 31, 32, 33],
 [ 0,  2,  3, 21, 22],
 [ 0,  0,  3,  4, 11],
 [ 0,  0,  0,  4,  5],
 [ 0,  0,  0,  0,  5]]

>>> level = order = 0
>>> for size in range(1 + 2, n + 1):
...     level += 10
...     order = 0
        # 0, 1, 2, 3, 4; n == 5, size == 3
        # => set == {(0,1,2),(1,2,3),(2,3,4)}
        # => i < 3
        # => `i < n - size + 1` or `i <= n - size`
...     for x in range(n - size + 1):
...             order += 1
...             y = x + size - 1
...             arr[x][y] = level + order
>>> arr
[[ 1,  2, 11, 21, 31],
 [ 0,  2,  3, 12, 22],
 [ 0,  0,  3,  4, 13],
 [ 0,  0,  0,  4,  5],
 [ 0,  0,  0,  0,  5]]
```
