function isValidWalk(walk) {
  if (walk.length != 10) {
    return false
  }

  let dx = 0
  let dy = 0

  walk.forEach(c => {
    switch (c) {
      case 'n':
        dy++
        break
      case 's':
        dy--
        break
      case 'e':
        dx++
        break
      case 'w':
        dx--
        break
      default:
        return false
    }
  })

  return dx === 0 && dy === 0
}
