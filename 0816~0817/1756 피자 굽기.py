# 참고 사이트 : https://rhdtka21.tistory.com/129


# def binary_search(start, end, target, array):
#     idx = -1

#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] >= target:
#             idx = mid
#             start = mid + 1
#         else:
#             end = mid - 1

#     return idx + 1


def main():
    for i in range(1, d):
        oven[i] = min(oven[i], oven[i-1])
    oven.reverse()

    # bottom = len(oven)

    # for pd in dough:
    #     depth = binary_search(0, bottom-1, pd, oven[:bottom])
    #     bottom = depth - 1

    # print(depth)

    dough_idx = 0
    depth = 0
    for i in range(d):
        if dough_idx > n-1:
            print(d - (depth - 1))
            return

        if dough[dough_idx] <= oven[depth]:
            dough_idx += 1

        depth += 1
        
    print(0)


if __name__ == "__main__":
    d, n = map(int, input().split())
    oven = list(map(int, input().split()))
    dough = list(map(int, input().split()))

    main()
