import sys
input = sys.stdin.readline

def path_sum(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]

def main():
    n = int(input().strip())  # 첫 번째 줄에서 n을 읽어옵니다.
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print(path_sum(triangle))

if __name__ == "__main__":
    main()
