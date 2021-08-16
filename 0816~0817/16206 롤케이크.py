def main():
    cakes.sort()
    cakes.sort(key=lambda x: str(x)[-1])

    answer = 0
    chance = m

    for cake in cakes:
        if cake == 10:
            answer += 1
        elif cake > 10 and chance > 0:
            div, mod = divmod(cake, 10)

            if mod == 0:
                cnt = min(div - 1, chance)

                if chance >= div - 1:
                    answer += 1
            else:
                cnt = min(div, chance)

            chance -= cnt
            answer += cnt

    print(answer)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cakes = list(map(int, input().split()))

    main()
