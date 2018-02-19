Python Syntax Note
======

## General

### Difference between `is` and `==`

`is` will return True if two variables point to the same object,
`==` if the objects referred to by the variables are equal.

- example in `str` and `bytes`

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

- example in `list`

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False
```

### Always ensures that shared vars are **IMMUTABLE**

in class

```python
# bad
>>> class TestClass:
...     x = {}
>>> a = TestClass()
>>> b = TestClass()
>>> a.x
{}
>>> a.x[1] = 2
>>> b.x
{1: 2}

# good
>>> class TestClass:
...     x = None
...     def __init__(self):
...             self.x = {}
>>> a = TestClass()
>>> b = TestClass()
>>> a.x
{}
>>> a.x[1] = 2
>>> b.x
{}
```

in func

```python
# bad
>>> def test_func(x=[]):
...     x.append(1)
...     return x
>>> test_func()
[1]
>>> test_func()
[1, 1]

# good
>>> def test_func(x=None):
...     if x is None:
...             x = []
...     x.append(1)
...     return x
>>> test_func()
[1]
>>> test_func()
[1]
```

### Hoisting

```python
# hoisting is in `for`, `if`, `while`
>>> a
NameError: name 'a' is not defined
>>> i
NameError: name 'i' is not defined
>>> for i in range(10):
...     a = 123
>>> a
123
>>> i
9

# hoisting is NOT in list comprehensions
>>> b
NameError: name 'b' is not defined
>>> [b for b in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b
NameError: name 'b' is not defined

# hoisting is NOT in `class`, `function`
>>> c
NameError: name 'c' is not defined
>>> def test(a = 1):
...     c = 2
>>> test()
>>> a
NameError: name 'a' is not defined
>>> c
NameError: name 'c' is not defined
```

## String `str`, `bytes`

### To find index

```python
>>> 'abc'.find('b')
1
>>> 'abc'.find('z')
-1
```

## Number `int`, `float`

### Using cascade comparison

```python
>>> 0 <= 2 < 3
True
>>> 0 <= 4 < 3
False
```

### Be careful of the division

```python
# Python 2
>>> 3 // 2
1
>>> 3 / 2
1
# to parse the result as float
>>> 3 / 2.0
1.5

# Python 3
>>> 3 // 2
1
>>> 3 / 2
1.5
```

conclusion:

```python
# need int
>>> 3 // 2
1

# need float
>>> 3 / 2.0
1.5
```

### Infinity

```python
# positive infinite
>>> float('inf')
inf

# negative infinite
>>> float('-inf')
-inf
```

## List `list`

## Iteration

```python
>>> A = [['a', 'b'], ['c', 'd']]
>>> A
[['a', 'b'], ['c', 'd']]
>>> B = map(''.join, A)
>>> B
<map object at 0x10e901da0>
>>> list(B)
['ab', 'cd']
```

### To find index

```python
>>> ['a', 'b', 'c'].index('b')
1
>>> ['a', 'b', 'c'].index('z')
ValueError: 'z' is not in list
```

### To sort list

```python
>>> l = [(2,3), (2,-3), (-2,3), (-2,-3)]

# 1 key
>>> sorted(l, key=lambda i: i[0])
[(-2, 3), (-2, -3), (2, 3), (2, -3)]

# 2+ keys
>>> sorted(l, key=lambda i: (i[0], i[1]))  # that is, `key=lambda i: i`
[(-2, -3), (-2, 3), (2, -3), (2, 3)]
```

### To reverse list

```python
>>> origin = [100, 1, 1000, 10]

>>> a = origin[:]
>>> a.sort(reverse=True)
>>> a
[1000, 100, 10, 1]    # sorting involved
>>> a is a
True

>>> b = origin[:]
>>> _b = sorted(b, reverse=True)
>>> _b
[1000, 100, 10, 1]    # sorting involved
>>> b is _b
False

>>> c = origin[:]
>>> _c = reversed(c)  # <list_reverseiterator object>
>>> list(_c)
[10, 1000, 1, 100]    # only reversed
>>> c is _c
False

>>> d = origin[:]
>>> _d = d[::-1]
>>> _d
[10, 1000, 1, 100]    # only reversed
>>> d is _d
False
```

### To extend list

```python
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> a.extend((4, 5, 6))
>>> a
[1, 2, 3, 4, 5, 6]
```

### To extend list with existing items

Note that this is copying the pointer, not value, that is,
the children must be **IMMUTABLE** in the list.

```python
>>> [1] * 3 * 3
[1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

>>> A = [[0] * 3] * 3
>>> A
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> A[0][1] = 1
>>> A
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
```

### To extend existing list and create new one

```python
>>> a = [1]
>>> b = a + [2]
>>> a is b
False
```

### To override mutable variable and keep the pointer if need

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

### To clone a list

```python
>>> a = [1, 2, 3]

# shallow clone
>>> b = a
>>> b is a
True
>>> b = a[:]
>>> b is a
False

# shallow clone
>>> c = a
>>> c is a
True
>>> c = a + []
>>> c is a
False

# deep clone
>>> a = [{'a': 1}]
>>> from copy import deepcopy
>>> b = deepcopy(a)
>>> a[0]['a'] = 2
>>> a, b
([{'a': 2}], [{'a': 1}])
```

## Dict `dict`

### Immutable Dict

```python
# set
>>> from collections import namedtuple
>>> ImmutableDict = namedtuple('ImmutableDict', ['k1', 'k2'])
>>> D = ImmutableDict(1, 2)
>>> D
ImmutableDict(k1=1, k2=2)

# get
>>> getattr(D, 'k1', -1)
1
>>> getattr(D, 'k3', -1)
-1
```

### Multi-dimensional indexing in dict

note that, since `tuple` is also **IMMUTABLE**.

```python
>>> d = {}
>>> d[1, 2, 3] = 1
>>> d[1, 2, 3]
1
>>> d[(1, 2, 3)]
1
>>> d
{(1, 2, 3): 1}
```

### To clone a dict

```python
>>> a = {'a': 1, 'b': 2}

# extend
>>> a.update({'c': 3, 'd': {'e': 4}})
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': {'e': 4}}

# shallow clone
>>> b = a.copy()
>>> a, b
({'a': 1, 'b': 2, 'c': 3, 'd': {'e': 4}}, {'a': 1, 'b': 2, 'c': 3, 'd': {'e': 4}})
>>> a['a'] = 99
>>> a['d']['e'] = 99
>>> a, b
({'a': 99, 'b': 2, 'c': 3, 'd': {'e': 99}}, {'a': 1, 'b': 2, 'c': 3, 'd': {'e': 99}})

# deep clone
>>> from copy import deepcopy
>>> b = deepcopy(a)
>>> a, b
({'a': 99, 'b': 2, 'c': 3, 'd': {'e': 99}}, {'a': 99, 'b': 2, 'c': 3, 'd': {'e': 99}})
>>> a['a'] = 111
>>> a['d']['e'] = 111
>>> a, b
({'a': 111, 'b': 2, 'c': 3, 'd': {'e': 111}}, {'a': 99, 'b': 2, 'c': 3, 'd': {'e': 99}})
```
