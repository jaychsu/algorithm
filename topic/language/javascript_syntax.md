JavaScript Syntax Note
======

## `Object`

### To check a key is in object

```js
// `obj.hasOwnProperty`
// check only the obj instance
> obj.hasOwnProperty('key')


// `in` operator
// check the whole prototype chain
> 'key' in obj

> const someKey = 'key'
> someKey in obj
```

## `Array`

### To init array with fixed length

Note that, the inited value passed into `fill` must be **IMMUTABLE**,
otherwise we can use `map` to init with mutable value.

```js
> new Array(3).fill(0)
[ 0, 0, 0 ]
> new Array(3).fill(0).map(_ => new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
```

Explanation:

```js
> let nums

// bad
> nums = new Array(3).fill(new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
> nums[0][0] = 1
1
> nums
[ [ 1, 0, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ] ]

// good
> nums = new Array(3).fill(0).map(_ => new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
> nums[0][0] = 1
1
> nums
[ [ 1, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
```

### To sort

The default sorting is by **alphabetical order**.
You can also indicate a comparator if you want to sort it by custom order.

```js
> const nums = [1, 2, 4, 6, 4, 2, 2, 5, 1, 11, 22, 2, 3, 44]
undefined
> nums.sort()
[ 1, 1, 11, 2, 2, 2, 2, 22, 3, 4, 4, 44, 5, 6 ]
> nums.sort((a, b) => a - b)
[ 1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6, 11, 22, 44 ]
> nums.sort((a, b) => b - a)
[ 44, 22, 11, 6, 5, 4, 4, 3, 2, 2, 2, 2, 1, 1 ]
```

### To override a existing array

```js
> let nums
undefined
> nums = [2, 1, 3, 4, 1, 2]
[ 2, 1, 3, 4, 1, 2 ]
> nums.splice(0, nums.length, ...[5, 6, 7, 1, 2, 3])
[ 2, 1, 3, 4, 1, 2 ]
> nums
[ 5, 6, 7, 1, 2, 3 ]
> nums.splice(0, nums.length)
[ 5, 6, 7, 1, 2, 3 ]
> nums
[]
```

## `String`

### To convert a string-number to a real number

```js
> +'123'
123
> +'-123'
-123
> -'123'
-123
> -'+123'
-123
> +'0'
0
> +'1'
1
> +'0.123'
0.123
> +'0.123a'
NaN
> +'0.123/2'
NaN
```

## `Boolean`

### To convert a boolean to `1` or `0`

```js
> +true
1
> +false
0
```

## `Set`

## `Map`
