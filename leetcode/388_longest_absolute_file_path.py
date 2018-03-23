"""
Main Concept:

if meet file, record the maximum size of the abs path `root/dir/file`
if meet dir, save current size for `root/dir`

for files:
two cases are at same depth
1. for hidden files
2. for extension in file


for dirs:
do NOT save the max size in each depth
since the children in same depth
may be under different parent

- root
  - p1
    - f-loooooong-1
  - p2
    - f-short-2

there is error in that case if save the max size
"""


class Solution:
    def lengthLongestPath(self, path):
        """
        :type path: str
        :rtype: int
        """
        ans = 0
        if not path:
            return ans

        dep2size = {0: 0}

        for line in path.split('\n'):
            name = line.lstrip('\t')
            size = len(name)
            depth = len(line) - len(name)

            if '.' in name:
                ans = max(ans, dep2size[depth] + size)
            else:
                dep2size[depth + 1] = dep2size[depth] + size + 1

        return ans
