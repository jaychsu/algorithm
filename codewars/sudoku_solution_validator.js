function validSolution(board) {
  if ( !Array.isArray(board)
    || !Array.isArray(board[0])
    || board.length !== board[0].length) {
    return false
  }

  const n = board.length
  const g = Math.sqrt(n)  // group counts

  if (g % 1 !== 0) return false  // check its square root

  const cnts = new Array(n).fill(0)
  let cnt = 0
  let i, j, x, y

  for (x = 0; x < n; x++) {
    for (y = 0; y < n; y++) {
      if (board[x][y] <= 0 || board[x][y] > n) return false
      if (cnts[board[x][y] - 1] !== cnt) return false
      cnts[board[x][y] - 1] += 1
    }
    cnt += 1

    for (y = 0; y < n; y++) {
      if (board[y][x] <= 0 || board[y][x] > n) return false
      if (cnts[board[y][x] - 1] !== cnt) return false
      cnts[board[y][x] - 1] += 1
    }
    cnt += 1
  }

  let x_from, x_to, y_from, y_to

  for (i = 0; i < g; i++) {
    for (j = 0; j < g; j++) {
      x_from = i * g
      x_to = i * g + g
      y_from = j * g
      y_to = j * g + g
      for (x = x_from; x < x_to; x++) {
        for (y = y_from; y < y_to; y++) {
          if (cnts[board[x][y] - 1] !== cnt) return false
          cnts[board[x][y] - 1] += 1
        }
      }
      cnt += 1
    }
  }

  return true
}
