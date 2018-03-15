function isPrime(num) {
  if (!num || num <= 1) return false

  const factors = [2, 3, 5, 7, 9, 11, 13, 17, 19].filter(base => {
    if (num <= base) return false
    if (num % base === 0) return true
    return false
  })

  return factors.length === 0
}
