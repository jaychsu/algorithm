function whoIsNext(names, r) {
  let total = names.length

  while (r > total) {
    r -= total
    total *= 2
  }

  return names[parseInt(names.length * (r - 1) / total)]
}
