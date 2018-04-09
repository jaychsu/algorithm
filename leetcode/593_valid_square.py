class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ps = []

        for p in (p1, p2, p3, p4):
            if not p:
                return False

            ps.append(p)

        ps.sort()

        # 0: lb, 1: lt, 2:rb, 3: rt
        l01 = self.get_distance(ps[0], ps[1])
        l02 = self.get_distance(ps[0], ps[2])
        l13 = self.get_distance(ps[1], ps[3])
        l23 = self.get_distance(ps[2], ps[3])

        l03 = self.get_distance(ps[0], ps[3])
        l12 = self.get_distance(ps[1], ps[2])

        return all((
            l01 == l02 == l13 == l23 > 0,
            l03 == l12,
        ))

    def get_distance(self, a, b):
        """
        find the size of 'ab'
        """
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return (dx * dx + dy * dy) ** 0.5
