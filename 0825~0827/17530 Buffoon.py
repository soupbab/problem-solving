import sys


def main():
    myScore = score[0]
    for s in score[1:]:
        if s > myScore:
            print("N")
            return
    else:
        print("S")


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    score = []
    for _ in range(N):
        score.append(int(input()))

    main()
    