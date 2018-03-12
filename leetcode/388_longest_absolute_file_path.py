class Solution:
    def lengthLongestPath(self, path):
        """
        :type path: str
        :rtype: int
        """
        if not path:
            return 0

        ans = 0
        dep2size = {0: 0}

        for line in path.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                # two cases are at same depth
                # 1. for hidden files
                # 2. for extension in file
                ans = max(ans, dep2size[depth] + len(name))
            else:
                # do NOT save the max size in each depth
                # since the children in same depth
                # may be under different parent
                #
                # - root
                #   - p1
                #     - f-loooooong-1
                #   - p2
                #     - f-short-2
                #
                # there is error in that case if save the max size
                dep2size[depth + 1] = dep2size[depth] + len(name) + 1

        return ans
