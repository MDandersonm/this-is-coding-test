# class Solution:
#     MOD = 1_000_000_007
#
#     def solution(self, n, k):
#         # dp[jump][pos]: jump번 점프하여 pos의 위치에 도착하는 방법의 가짓수
#         dp = [[0] * (n + 1) for _ in range(k + 1)]
#
#
#         for jump in range(1, k + 1):
#             for pos in range(1, n + 1):
#                 for prevJump in range(1, pos):
#                     dp[jump][pos] += dp[jump - 1][pos - prevJump]
#                     dp[jump][pos] %= self.MOD
#                 if jump == 1 and pos <= n:  # 첫번째 점프는 어떤 거리든지 점프할 수 있음
#                     dp[jump][pos] = 1
#                 print("jump", jump, "pos", pos, "dp[jump][pos]", dp[jump][pos] )
#
#         return dp[k][n]
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.solution(9, 3))  # 3
#     # print(sol.solution(10, 2))  # 4
#     # print(sol.solution(9, 4))  # 0
class Solution:
    MOD = 1_000_000_007
    def solution(self, n, k):
        # dp[jump][pos][prev]: jump번 점프하여 prev만큼 점프(이전 점프거리)하여 pos의 위치에 도착하는 방법의 가짓수
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(k + 1)]
        # 첫 번째 점프는 어떤 거리든지 점프할 수 있음
        for i in range(1, n + 1):
            dp[1][i][i] = 1 # i=2인경우 점프 1회차에 2위치에 도달 그때 점프거리가2니까 [1][2][2] 로 쓰는거

        for jump in range(2, k + 1):
            for pos in range(1, n + 1):
                for prevJump in range(1, pos):
                    # print("dp[jump - 1][pos - prevJump][:prevJump]",dp[jump - 1][pos - prevJump][:prevJump])
                    dp[jump][pos][prevJump] = sum(dp[jump - 1][pos - prevJump][:prevJump]) % self.MOD
                    # print("jump", jump, "pos", pos,"prevJump",prevJump, "dp[jump][pos][prevJump]", dp[jump][pos][prevJump])

        # 마지막 위치 n에서 k번 점프한 경우의 수를 모두 더한다.
        return sum(dp[k][n]) % self.MOD


if __name__ == "__main__":
    sol = Solution()
    print(sol.solution(9, 3))  # 3
    print(sol.solution(10, 2))  # 4
    print(sol.solution(9, 4))  # 0
