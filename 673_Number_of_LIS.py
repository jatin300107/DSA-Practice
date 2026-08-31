from typing import List
nums = [1,3,5,4,7]

def findNumberOfLIS( nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]

                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        max_lis = max(dp)
        return sum(count[i] for i in range(n) if dp[i] == max_lis)
            
            

result = findNumberOfLIS(nums)