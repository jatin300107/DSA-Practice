from typing import List

envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]

# O(n2) Approach 
def maxEnvelopes( envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes = sorted(envelopes, key=lambda x: x[0])
        dp = [1] * (n+1)
        for i in range(n):
            for j in range(n):
                if envelopes[i][0] > envelopes[j][0]  and envelopes[i][1] >  envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j] +1)

        print(max(dp))

maxEnvelopes(envelopes=envelopes)