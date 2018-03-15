function reverseWords(s) {
  return s.split(' ').map(word => {
    return word.split('').reverse().join('')
  }).join(' ')
}
