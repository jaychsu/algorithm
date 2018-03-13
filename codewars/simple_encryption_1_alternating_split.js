function encrypt(text, n) {
  if (!text || !n || n < 0) return text

  const TEXT_SIZE = text.length

  while (n--) {
    const _text = []

    for (let i = 1; i < TEXT_SIZE; i += 2) {
      _text.push(text[i])
    }

    for (let i = 0; i < TEXT_SIZE; i += 2) {
      _text.push(text[i])
    }

    text = _text.join('')
  }

  return text
}

function decrypt(text, n) {
  if (!text || !n || n < 0) return text

  const TEXT_SIZE = text.length
  const HALF_TEXT_SIZE = parseInt(text.length / 2)

  while (n--) {
    const _text = []

    for (let i = 0; i < HALF_TEXT_SIZE + 1; i++) {
      if (HALF_TEXT_SIZE + i < TEXT_SIZE) {
        _text.push(text[HALF_TEXT_SIZE + i])
      }

      if (i < HALF_TEXT_SIZE) {
        _text.push(text[i])
      }
    }

    text = _text.join('')
  }

  return text
}
