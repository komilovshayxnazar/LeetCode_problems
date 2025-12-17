from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp0 = [-float('inf')] * (k + 1)
        dp1 = [-float('inf')] * (k + 1)
        dp2 = [-float('inf')] * (k + 1)
        dp0[0] = 0

        for price in prices:
            new_dp0 = dp0[:]
            new_dp1 = dp1[:]
            new_dp2 = dp2[:]

            for t in range(k + 1):
                if dp0[t] != -float('inf'):
                    new_dp1[t] = max(new_dp1[t], dp0[t] - price)

                if dp0[t] != -float('inf'):
                    new_dp2[t] = max(new_dp2[t], dp0[t] + price)

                if dp1[t] != -float('inf') and t < k:
                    new_dp0[t + 1] = max(new_dp0[t + 1], dp1[t] + price)

                if dp2[t] != -float('inf') and t < k:
                    new_dp0[t + 1] = max(new_dp0[t + 1], dp2[t] - price)

                new_dp1[t] = max(new_dp1[t], dp1[t])
                new_dp2[t] = max(new_dp2[t], dp2[t])

            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2

        return max(dp0)