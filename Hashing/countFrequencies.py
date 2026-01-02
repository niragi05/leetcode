class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        res = []
        for num, count in freq.items():
            res.append([num, count])

        return res
