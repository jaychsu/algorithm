Binary search
======

```python
>>> arr = [True, True, True, True, False, False]
>>> left, mid, right = 0, 0, len(arr) - 1

# to prevent dead cycle
>>> while left + 1 < right:
...
...     # to avoid int overflow, but it could be ignored in `Python 3`
...     mid = left + (right - left) // 2
...
...     if arr[mid]:
...         left = mid
...     else:
...         right = mid

# check again the end point, and fetch what we need
>>> left if arr[left] else right
3
```
