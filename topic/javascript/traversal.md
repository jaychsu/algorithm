Traversal
======

## To simulate a queue

It's also a good example to show how the pointer works for the loop.

```js
> const queue = [1]
undefined
> for (let i = 0; i < queue.length; i++) {
...   if (i === 5) break
...   queue.push(i)
... }
undefined
> queue
[ 1, 0, 1, 2, 3, 4 ]
```

```js
> const queue = [1]
undefined
> let i = 0
undefined
> queue.forEach(num => {
...   if (i === 5) return
...   queue.push(i)
... })
undefined
> queue
[ 1, 0 ]
```

## To do BFS in level

```js
> const queue = [[0, 0]]
undefined
> const _queue = []
undefined
> const delta = [
...   [0, -1], [0, 1],
...   [-1, 0], [1, 0],
... ]
undefined
>
> const visited = {'0,0': 0}
undefined
> let steps = 0
undefined
> let i, x, y, _x, _y, key
undefined
>
> while (queue.length && steps < 2) {
... steps += 1
...
... for (i = 0; i < queue.length; i++) {
...   [x, y] = queue[i]
...
...   delta.forEach(([dx, dy]) => {
...     _x = x + dx
...     _y = y + dy
...     key = `${_x},${_y}`
...
...     if (visited[key] < steps) return
...
...     visited[key] = steps
...     _queue.push([_x, _y])
...   })
... }
...
... queue.splice(0, queue.length, ..._queue)
... _queue.splice(0, _queue.length)
... }
[ [ 0, -2 ], [ -1, -1 ], [ 1, -1 ], [ 0, 2 ],
  [ -1, 1 ], [ 1, 1 ], [ -1, -1 ], [ -1, 1 ],
  [ -2, 0 ], [ 1, -1 ], [ 1, 1 ], [ 2, 0 ] ]
>
> queue
[ [ 0, -2 ], [ -1, -1 ], [ 1, -1 ], [ 0, 2 ],
  [ -1, 1 ], [ 1, 1 ], [ -1, -1 ], [ -1, 1 ],
  [ -2, 0 ], [ 1, -1 ], [ 1, 1 ], [ 2, 0 ] ]
> visited
{ '0,0': 0, '0,-1': 1, '0,1': 1, '-1,0': 1,
  '1,0': 1, '0,-2': 2, '-1,-1': 2, '1,-1': 2,
  '0,2': 2, '-1,1': 2, '1,1': 2, '-2,0': 2, '2,0': 2 }
```
