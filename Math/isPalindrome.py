class Solution:
    def isPalindrome(self, n):
        rev = 0
        rem = n

        while rem > 0:
            last = rem % 10
            rev = rev * 10 + last

            rem = rem // 10

        return n == rev