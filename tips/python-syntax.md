- To extend list with existing items

```python
>>> [1] * 3 * 3
[1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

- Be careful of the Unicode string

```python
# Python `2.7.13`, `2.7.14`
>>> u'test' == 'test'
True
>>> u'test' is 'test'
False

# Python `3.6.0`, `3.6.3`
>>> u'test' == 'test'
True
>>> u'test' is 'test'
True
```

- Be careful of the division

```python
# Python 2
>>> 3 / 2
1
>>> 3 // 2
1

# to parse the result as float
>>> 3 * 1.0 / 2
1.5


# Python 3
>>> 3 / 2
1.5
>>> 3 // 2
1
```

- Use cascade comparison

```python
>>> 0 <= 2 < 3
True
>>> 0 <= 4 < 3
False
```

- Override mutable variable and keep the pointer if need

```python
>>> a = b = [1, 2, 3]
>>> a is b
True

>>> b[:] = [4, 5, 6]
>>> a
[4, 5, 6]
>>> a is b
True

>>> b = [7, 8, 9]
>>> a
[4, 5, 6]
>>> a is b
False
```

- Infinity

```python
# positive infinite
>>> float('inf')
inf

# negative infinite
>>> float('-inf')
-inf
```
