class Solution:
    def mostFrequentElement(self, nums):
        # Solution 1:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        best_elem = None
        best_count = 0

        for x, c in freq.items():
            if c > best_count or (c == best_count and (best_elem is None or x < best_elem)):
                best_count = c
                best_elem = x

        return best_elem