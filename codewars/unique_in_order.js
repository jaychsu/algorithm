function uniqueInOrder(iterable) {
  if (!iterable) {
    return []
  }

  const ans = [iterable[0]]

  for (let i = 1; i < iterable.length; i++) {
    if (iterable[i] != ans[ans.length - 1]) {
      ans.push(iterable[i])
    }
  }

  return ans
}
