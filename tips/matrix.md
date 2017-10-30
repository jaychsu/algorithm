- To convert the 2D matrix to 1D line

```python
# For any m * n matrix
# 0 <= x < m, 0 <= y < n
# The cell at `[i, j]` can be mapped to `k` in line
k = i * n + j
```

- To iterate around the current cell (means to visit the cell at the top/bottom/left/right)

```python
x, y = 1, 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(4):
    _x = x + dx[i]
    _y = y + dy[i]
# 0, r: (2, 1)
# 1, l: (0, 1)
# 2, b: (1, 2)
# 3, t: (1, 0)
```

- To avoid returning along the original path, just simply set the last visited cell to `'#'`

see [132-word-search-ii.py](../lintcode/132-word-search-ii.py)
