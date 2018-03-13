function sqInRect(lng, wdth) {
  if (!lng || !wdth || lng === wdth) return null

  const ans = []

  while (lng != 1 || wdth != 1) {
    if (lng > wdth) {
      ans.push(wdth)
      lng -= wdth
    } else if (lng < wdth) {
      ans.push(lng)
      wdth -= lng
    } else {
      ans.push(lng)
      break
    }
  }

  if (lng == 1 && wdth == 1) {
    ans.push(1)
  }

  return ans
}
