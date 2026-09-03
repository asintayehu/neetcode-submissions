class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map count to array of numbers

        count = [[] for i in range(len(nums) + 1)]
        count_map = {}
        answer= []

        # count frequency

        for i in range(len(nums)):

            if nums[i] not in count_map:
                count_map[nums[i]]= 1
            else:
                count_map[nums[i]]+= 1
    
        for n, c in count_map.items():
            count[c].append(n)
        
        for idx in range(len(count)-1, 0, -1):
            for number in count[idx]:
                if len(answer) == k:
                    return answer
                else:
                    answer.append(number)
        

        return answer
