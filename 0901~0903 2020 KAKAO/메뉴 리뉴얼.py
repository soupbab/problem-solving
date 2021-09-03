from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for i in course:
        result = defaultdict(int)

        for order in orders:
            for combination in combinations(order, i):
                result["".join(sorted(list(combination)))] += 1

        if result.values():
            max_cnt = max(result.values())
            if max_cnt > 1:
                for key, value in result.items():
                    if value == max_cnt:
                        answer.append(key)

    return sorted(answer)
