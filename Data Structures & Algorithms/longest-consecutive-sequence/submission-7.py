class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set= set(nums)
        ans= 0
        for item in num_set:
            if (item-1) not in num_set:
                sequence_length= 0
                while (item + sequence_length) in num_set:
                    sequence_length+= 1
                ans= max(sequence_length, ans)
        return ans