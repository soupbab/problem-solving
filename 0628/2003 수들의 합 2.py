def find_sequence():
    count = 0

    if sum(sequence) > m:
        for i in range(n):
            accum = sequence[i]
            j = i + 1

            while accum <= m:
                if accum == m:
                    count += 1
                    break
                else:
                    if j < n:
                        accum += sequence[j]
                        j += 1
                    else:
                        break
    elif sum(sequence) == m:
        count = 1

    print(count)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    sequence = list(map(int, input().strip().split()))

    find_sequence()