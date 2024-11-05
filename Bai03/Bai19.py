def count_ways_to_make_change(S, N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for coin in S:
        for i in range(int(coin), N + 1):
            dp[i] += dp[i - int(coin)]
    return dp[N]
N = int(input())
S=[]
chuoi = str(input("Nhập tất cả xu đổi (a,b,c): "))
S=chuoi.split(",")
print("Có", count_ways_to_make_change(S,N), "nghiệm")