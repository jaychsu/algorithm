function deleteNth(nums, n) {
  const freq = {}

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]

    if (!freq.hasOwnProperty(num)) {
      freq[num] = 0
    }

    freq[num] += 1
  }

  for (let i = nums.length - 1; i >= 0; i--) {
    const num = nums[i]

    if (freq[num] <= n) {
      continue
    }

    nums.splice(i, 1)
    freq[num] -= 1
  }

  return nums
}
