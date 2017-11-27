The time-complexity of various operations in **CPython**
======

note that,

1. **CPython** is the official and most widespread version
2. `n = len(data)`

## Basic

| Operation                    | Example              | Complexity | Notes                                    |
| ---------------------------- | -------------------- | ---------- | ---------------------------------------- |
| binding immutable value      | `a = 1`              | $O(1)$     |                                          |
| simple operators on integers | `1 + 1`,<br>`2 == 2` | $O(1)$     | assume small integers unless explicitly told otherwise |

## List, Tuple

| Operation             | Example               | Complexity    | Notes                                    |
| --------------------- | --------------------- | ------------- | ---------------------------------------- |
| index                 | `l[i]`                | $O(1)$        |                                          |
| store                 | `l[i] = 0`            | $O(1)$        |                                          |
| length                | `len(l)`              | $O(1)$        |                                          |
| append                | `l.append(5)`         | $O(1)$        |                                          |
| pop                   | `l.pop()`             | $O(1)$        | same as `l.pop(-1)`, popping at end      |
| clear                 | `l.clear()`           | $O(1)$        | similar to `l = []`                      |
| slice                 | `l[a:b]`              | $O(b-a)$      | `l[1:5]` -> $O(l)$<br>`l[:]` -> $O(len(l)-0)=O(n)$ |
| extend                | `l.extend(l2)`        | $O(m)$        | `m = len(l2)`                            |
| construction iterable | `list(l)`             | $O(n)$        |                                          |
| check `==`, `!=`      | `l == l2`             | $O(n)$        | note that, `is` -> $O(1)$                |
| insert                | `l[a:b] = l2`         | $O(n)$        |                                          |
| delete                | `del l[i]`            | $O(n)$        |                                          |
| containment           | `v in l`/`v not in l` | $O(n)$        | searches list                            |
| copy                  | `l.copy()`            | $O(n)$        | same as `l[:]` which is $O(n)$           |
| remove                | `l.remove(v)`         | $O(n)$        | remove `v` from `l` if `v` in `l` otherwise raise an exception |
| pop                   | `l.pop(i)`            | $O(n)$        | $O(n-i)$<br>`l.pop(0)` -> $O(n)$         |
| extreme value         | `min(l)`/`max(l)`     | $O(n)$        | searches list                            |
| reverse               | `l.reverse()`         | $O(n)$        |                                          |
| iteration             | `for v in l:`         | $O(n)$        |                                          |
| sort                  | `l.sort()`            | $O(n\log(n))$ | `key`/`reverse` mostly doesn't change    |
| multiply              | `k * l`               | $O(k×n)$      |                                          |

## Set

| Operation | Example | Complexity | Notes |
| --------- | ------- | ---------- | ----- |
|           |         |            |       |

## Dict

| Operation | Example | Complexity | Notes |
| --------- | ------- | ---------- | ----- |
|           |         |            |       |

## Reference

- [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
