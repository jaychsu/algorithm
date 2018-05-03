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

// error
> nums = new Array(3).fill(new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
> nums[0][0] = 1
1
> nums
[ [ 1, 0, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ] ]

// correct
> nums = new Array(3).fill(0).map(_ => new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
> nums[0][0] = 1
1
> nums
[ [ 1, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
```
