## Steps to find solutions

```
TODO
```

## Print Paths

steps:

1. use a list, usually named `pi`, to record the previous index to backtrack when calculating `dp`
2. backtrack to the first index, and save the visited index in `paths`
3. print `paths`

1D example:

- [lintcode/397_longest_increasing_continuous_subsequence.py](../lintcode/397_longest_increasing_continuous_subsequence.py)
- [lintcode/76_longest_increasing_subsequence.py](../lintcode/76_longest_increasing_subsequence.py)

2D example:

- [lintcode/168_burst_balloons.py](../lintcode/168_burst_balloons.py)

## Rolling Array

to reduce the space complexity by one or more dimensions.

note that, **remember to INIT the value in rolling array to reuse it**.

there are two optimizations:

### if current `i` only depends on `i-k` row, just mod `k+1` to reduce size

note that, if you want to optimize two dimensions at the same time,
every child has to count twice and will lead to **high time complexity**.

example:

- [lintcode/515_paint_house.py](../lintcode/515_paint_house.py)
- [lintcode/534_house_robber_ii.py](../lintcode/534_house_robber_ii.py)
- [lintcode/119_edit_distance.py](../lintcode/119_edit_distance.py)

```python
# `i` only depends on `i - 1`
dp = [[0] * n for _ in range(2)]

prev = curr = 0
for i in range(n):
    prev = curr  # same as `(i - 1) % 2`
    curr = 1 - curr  # same as `i % 2`
```

### reduce 2D matrix to 1D list, if the order in calculation allow this

example:

- [lintcode/563_backpack_v.py](../lintcode/563_backpack_v.py)
