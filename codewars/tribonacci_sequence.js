function tribonacci(signature, n) {
  if (!n) return []

  const ans = signature.slice()

  for (let i = 3; i < n; i++) {
    ans.push(ans[i - 3] + ans[i - 2] + ans[i - 1])
  }

  return ans.slice(0, n)
}
