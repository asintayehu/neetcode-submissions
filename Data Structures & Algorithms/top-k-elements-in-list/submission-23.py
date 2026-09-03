from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n_prime= Counter(nums)

        common= n_prime.most_common(k)
        ans= []

        for i in range(0, k):
            ans.append(common[i][0])

        return ans
