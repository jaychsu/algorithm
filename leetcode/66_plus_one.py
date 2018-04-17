class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []

        if not digits:
            return ans

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            ans.append(carry % 10)
            carry //= 10

        if carry:
            ans.append(carry)

        ans.reverse()

        return ans


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []

        carry = 0
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            digits[i] = carry % 10
            carry //= 10

        if carry:
            digits.append(carry)

            for i in range(len(digits) - 1, 0, -1):
                digits[i], digits[i - 1] = digits[i - 1], digits[i]

        return digits
