class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        res = [[0, 359, 1]]
        if not isinstance(n, int) \
            or n < 2:
            return res
        ti = 0 # ti: target_index for the **upcoming** machine in results
        # mi: machine_index for the **upcoming** machines in results
        # for n is 5: got [1, 2, 3, 4]
        for mi in range(1, n):
            ti = 0
            # emi: existing_machine_index for the **existing** machines in results
            # for n is 5 and will add last machine: got [0, 1, 2, 3]
            for emi in range(mi):
                # Before adding each machine, check the current maximum partition
                if res[emi][1] - res[emi][0] > res[ti][1] - res[ti][0]:
                    ti = emi
            x, y = res[ti][0], res[ti][1]
            res[ti][1] = (x + y) / 2
            res.append([(x + y) / 2 + 1, y, mi + 1])
        return sorted(res, key=lambda item: item[0])
