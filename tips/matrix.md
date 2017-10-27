- To convert the 2D matrix to 1D line

```python
# For any m * n matrix
# The cell at `[i, j]` can be mapped to `k` in line
k = i * m + j
```

- To iterate around the current cell (means to visit the cell at the top/bottom/left/right)

```python
cell_at = (1, 1)
row_vector = [1, -1, 0, 0]
col_vector = [0, 0, 1, -1]
for dir in range(4):
    x = cell_at[0] + row_vector[dir]
    y = cell_at[1] + col_vector[dir]
# 0, r: (x, y) = (2, 1)
# 1, l: (x, y) = (0, 1)
# 2, b: (x, y) = (1, 2)
# 3, t: (x, y) = (1, 0)
```
