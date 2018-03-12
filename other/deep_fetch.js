function deepFetch(target, path, defaultValue = undefined) {
  if (!target || !Array.isArray(path)) {
    return defaultValue
  }

  return path.reduce((level, key) => (
    (level && level[key]) ? level[key] : defaultValue
  ), target)
}


module.exports = deepFetch
