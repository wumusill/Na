# 개미 전사

# 정수 N을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * n

# 모든 식량 정보 입력받기
l = list(map(int, input().split()))

# 다이나믹 프로그래밍 바텀업
dp[0] = l[0]
dp[1] = max(l[0], l[1])
for i in range(2, n):
    dp[i] = max(l[i] + dp[i-2], dp[i-1])

print(max(dp))