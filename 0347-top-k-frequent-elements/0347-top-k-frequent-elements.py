class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        # HashMap freq_count the key is the frequent count 
        # and value is number from nums
        freq_count = [[] for i in range(len(nums)+1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n,0)

        for num, c in num_count.items():
            freq_count[c].append(num)

        res = []
        for index in range(len(freq_count) -1, 0, -1):
            for num in freq_count[index]:
                res.append(num)
                if len(res) == k:
                    return res