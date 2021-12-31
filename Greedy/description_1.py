# 최소한의 동전으로 거스름돈 주기

N = int(input())
coin = [500, 100, 50, 10]
num_coin = 0
for i in coin:
    num_coin += N // i
    N %= i129
print(num_coin)