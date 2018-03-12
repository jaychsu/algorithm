const deepFetch = require('./deep_fetch')

test('It could deeply fetch props from target', () => {
  const target = {
    a: 1,
    b: 2,
    c: {
      d: 3,
      e: {
        f: 4,
        g: 5,
      },
    },
  }

  expect(deepFetch(target, ['b'])).toBe(2)
  expect(deepFetch(target, ['c', 'd'])).toBe(3)
  expect(deepFetch(target, ['c', 'e', 'f'])).toBe(4)
  expect(deepFetch(target, ['c', 'e', 'h'])).toBe(undefined)
  expect(deepFetch(target, ['c', 'e', 'h'], -1)).toBe(-1)
})
