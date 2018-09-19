Bit Manipulation
======

## Modulo

```python
>>> a & 1 == a % 2
True
```

## Division

```python
>>> a >> 1 == a // 2
True
```

## 0 -> 1, 1 -> 0

output 1 if input 0

```python
>>> True ^ 1
0
>>> 1 ^ 1
0
>>> False ^ 1
1
>>> 0 ^ 1
1
```

## To check a number is power of 2

if a number is power of 2, then there is only 1 in the bit format in the number.

```python
>>> [(num & (num - 1)) == 0 for num in (4, 5, 11, 16, 21, 29, 32)]
[True, False, False, True, False, False, True]
```
