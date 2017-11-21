- To convert the 2D matrix to 1D line

```python
# For any m * n matrix
# 0 <= x < m, 0 <= y < n
# The cell at `[i, j]` can be mapped to `k` in line
k = i * n + j
```

- To iterate around the current cell (means to visit the cell at the top/bottom/left/right)

```python
p = (1, 1)
vector = (
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
)
for dx, dy in vector:
    print(p[0] + dx, p[1] + dy)

# 0, l: (0, 1)
# 1, r: (2, 1)
# 2, t: (1, 0)
# 3, b: (1, 2)
```

- To avoid returning along the original path, just simply set the last visited cell to `'#'`

see [132-word-search-ii.py](../lintcode/132-word-search-ii.py)
