class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        results = [[0, 359, 1]]
        if not isinstance(n, int) or n < 2:
            return results
        # These are the indices for the **upcoming** machines in results
        # for n is 5: got [1, 2, 3, 4]
        for i in range(1, n):
            index = 0
            # These are the indices for the **existing** machines in results
            # for n is 5 and will add last machine: got [0, 1, 2, 3]
            for j in range(0, i):
                # Before adding each machine, check the current maximum partition
                if results[j][1] - results[j][0] > results[index][1] - results[index][0]:
                    index = j
            x, y = results[index][0], results[index][1]
            results[index][1] = (x + y) / 2
            results.append([(x + y) / 2 + 1, y, i+1])
        return sorted(results, key=lambda item: item[0])
