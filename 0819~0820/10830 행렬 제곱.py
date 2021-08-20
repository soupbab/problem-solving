from functools import reduce


def matmul(A, B):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            val = 0
            for k in range(n):
                val += A[i][k] * B[k][j]
            row.append(val % 1000)
        result.append(row)

    return result


def main():
    num_array = []
    pow_array = []
    target = b
    num = 1
    pow = 0

    while num * 2 < target:
        num *= 2
        pow += 1
    num_array.append(num)
    pow_array.append(pow)
    target -= num

    while target > 0:
        if target - num >= 0:
            num_array.append(num)
            pow_array.append(pow)
            target -= num
        else:
            num //= 2
            pow -= 1

    dp = [matrix]
    while len(dp) <= pow_array[0]:
        dp.append(matmul(dp[-1], dp[-1]))

    mat_array = []
    for p in pow_array:
        mat_array.append(dp[p])

    answer = reduce(matmul, mat_array)
    for a in answer:
        print(*a)


if __name__ == "__main__":
    n, b = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(lambda x: int(x) % 1000, input().split())))

    main()
