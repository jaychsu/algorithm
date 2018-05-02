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

```js
> new Array(3).fill(0)
[ 0, 0, 0 ]
> new Array(3).fill(new Array(3).fill(0))
[ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
```
