function iqTest(nums) {
  nums = nums.split(' ').map(c => +c & 1)

  for (let i = 2; i < nums.length; i++) {
    if (nums[0] ^ nums[i] && nums[1] ^ nums[i]) {
      return i + 1
    } else if (nums[i] ^ nums[0] && nums[1] ^ nums[0]) {
      return 1
    } else if (nums[0] ^ nums[1] && nums[i] ^ nums[1]) {
      return 2
    }
  }

  return -1
}
