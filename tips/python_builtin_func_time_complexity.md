The time-complexity of various operations in **CPython**
======

Note that,

1. **CPython** is the official and most widespread implementation
2. `n = len(data)`

## Basic

| Operation                    | Example              | Complexity | Notes                                    |
| ---------------------------- | -------------------- | ---------- | ---------------------------------------- |
| binding immutable value      | `a = 1`              | $O(1)$     |                                          |
| simple operators on integers | `1 + 1`,<br>`2 == 2` | $O(1)$     | assume small integers unless explicitly told otherwise<br>(whose values are small: e.g., under 12 digits) |

## List, Tuple

`tuple` support all operations that do not mutate the data structure (and with the same complexity classes).

When comparing two lists for equality, the complexity class above shows as $O(n)$, but in reality we would need to multiply this complexity by $O(==)$ where $O(==)$ is the complexity class for checking whether two values in the list are `==`. If they are ints, $O(==)$ would be $O(1)$; if they are strings, $O(==)$ in the worst case it would be $O(len(string))$. This issue applies any time an `==` check is done. We mostly will assume `==` checking on values in lists is $O(1)$: e.g., checking ints and small strings.

| Operation             | Example               | Complexity    | Notes                                    |
| --------------------- | --------------------- | ------------- | ---------------------------------------- |
| index                 | `l[i]`                | $O(1)$        |                                          |
| store                 | `l[i] = 0`            | $O(1)$        |                                          |
| length                | `len(l)`              | $O(1)$        |                                          |
| append                | `l.append(5)`         | $O(1)$        |                                          |
| pop                   | `l.pop()`             | $O(1)$        | same as `l.pop(-1)`, popping at end      |
| clear                 | `l.clear()`           | $O(1)$        | similar to `l = []`                      |
| slice                 | `l[a:b]`              | $O(b-a)$      | `l[1:5]` -> $O(l)$<br>`l[:]` -> $O(len(l)-0)=O(n)$ |
| extend                | `l.extend(t)`         | $O(m)$        | `m = len(t)`                             |
| construction iterable | `list(l)`             | $O(n)$        |                                          |
| check `==`, `!=`      | `l == t`              | $O(n)$        | note that, `is` -> $O(1)$, see [Difference between `is` and `==`](./python_syntax.md#difference-between-is-and-) |
| insert                | `l[a:b] = t`          | $O(n)$        |                                          |
| delete                | `del l[i]`            | $O(n)$        |                                          |
| containment           | `v in l`/`v not in l` | $O(n)$        | searches list                            |
| copy                  | `l.copy()`            | $O(n)$        | same as `l[:]` -> $O(n)$                 |
| remove                | `l.remove(v)`         | $O(n)$        | remove `v` from `l` if `v` in `l` otherwise raise an exception |
| pop                   | `l.pop(i)`            | $O(n)$        | $O(n-i)$<br>`l.pop(0)` -> $O(n)$         |
| extreme value         | `min(l)`/`max(l)`     | $O(n)$        | searches list                            |
| reverse               | `l.reverse()`         | $O(n)$        |                                          |
| iteration             | `for v in l:`         | $O(n)$        |                                          |
| sort                  | `l.sort()`            | $O(n\log(n))$ | `key`/`reverse` mostly doesn't change    |
| multiply              | `k * l`               | $O(k×n)$      |                                          |

## Set

`set` have many more operations that are $O(1)$ compared with lists and tuples. Not needing to keep values in a specific order in a set (which lists/tuples require) allows for faster set operations.

Frozen sets support all operations that do not mutate the data structure (and with the same complexity classes).

| Operation            | Example               | Complexity | Notes                                    |
| -------------------- | --------------------- | ---------- | ---------------------------------------- |
| length               | `len(s)`              | $O(1)$     |                                          |
| add                  | `s.add(5)`            | $O(1)$     |                                          |
| containment          | `v in s`/`v not in s` | $O(1)$     | compare to list/tuple -> $O(n)$          |
| remove               | `s.remove(v)`         | $O(1)$     | remove `v` from `s` if `v` in `s` otherwise raise an exception<br>compare to list/tuple -> $O(n)$ |
| discard              | `s.discard(v)`        | $O(1)$     | remove `v` from `s` even `v` not in `s` -> no exception |
| pop                  | `s.pop()`             | $O(1)$     |                                          |
| clear                | `s.clear()`           | $O(1)$     | similar to `s = set()`                   |
| construction         | `set(l)`              | $O(n)$     | depends on length of iterable, that is `l` here |
| check `==`, `!=`     | `s != t`              | $O(n)$     | `len(s)` must be same as `len(t)`<br>if not, return False in $O(1)$ |
| `<=`/`<`             | `s <= t`              | $O(n)$     | issubset                                 |
| `>=`/`>`             | `s >= t`              | $O(m)$     | `m = len(t)`<br>issuperset `s >= t` == `t <= s` |
| union                | `s \| t`              | $O(m+n)$   |                                          |
| intersection         | `s & t`               | $O(m+n)$   |                                          |
| difference           | `s - t`               | $O(m+n)$   |                                          |
| symmetric difference | `s ^ t`               | $O(m+n)$   | see [Symmetric Difference @wikipedia](https://en.wikipedia.org/wiki/Symmetric_difference) |
| iteration            | `for v in s:`         | $O(n)$     |                                          |
| copy                 | `s.copy()`            | $O(n)$     |                                          |

## Dict

Most `dict` operations are $O(1)$.

`defaultdict` support all operations that dicts support, with the same complexity classes (because it inherits all the operations); this assumes that calling the constructor when a values isn't found in the defaultdict is $O(1)$ - which is true for `int()`, `list()`, `set()`, ... (the things we commonly use)

| Operation               | Example       | Complexity | Notes                                    |
| ----------------------- | ------------- | ---------- | ---------------------------------------- |
| index                   | `d[k]`        | $O(1)$     |                                          |
| store                   | `d[k] = v`    | $O(1)$     |                                          |
| length                  | `len(d)`      | $O(1)$     |                                          |
| delete                  | `del d[k]`    | $O(1)$     |                                          |
| `get`/`setdefault`      | `d.get()`     | $O(1)$     |                                          |
| pop                     | `d.pop(k)`    | $O(1)$     |                                          |
| pop item                | `d.popitem()` | $O(1)$     |                                          |
| clear                   | `d.clear()`   | $O(1)$     | similar to `s = {}` or `s = dict()`      |
| `keys`/`values`/`items` | `d.keys()`    | $O(1)$     |                                          |
| construction            | `dict(t)`     | $O(n)$     | `n = len(t)`<br>the interface of `t`: `Iterable[Iterable]`<br>example: `((1, 2), (2, 3), (4, 5), ('a', 6))` |
| iteration               | `for v in d:` | $O(n)$     | same as `for v in d.keys()`<br>all forms: `keys`, `values`, `items` |

## Reference

- [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
