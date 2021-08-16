def main():
    dp = [[0, 0], [0, 0], [1, 1], [2, 2], [2, 2]]
    
    while len(dp) <= n:
        if len(dp) % 3 == 0:
            dp.append([dp[-2][0] + 1, dp[-2][1] + 2])
        else:
            dp.append([dp[-2][0] + 1, dp[-2][1] + 1])
    
    print(*dp[n])


if __name__ == "__main__":
    n = int(input().rstrip())

    main()
