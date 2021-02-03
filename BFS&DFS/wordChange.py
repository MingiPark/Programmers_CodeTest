begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque as dq

#Boolean 결과 값을 가진다. True/False
transistable = lambda a, b: sum((1 if x != y else 0) for x, y in zip(a, b)) == 1


def solution1(begin, target, words):
    answer = 0

    q, d = dq(), dict()
    q.append((begin, 0))

    #{hit:{hot}}, {dog:{log,cog}}
    d[begin] = set(filter(lambda x: transistable(x, begin), words))

    for w in words:
        d[w] = set(filter(lambda x: transistable(x, w), words))

    while q:
        cur, answer = q.popleft()
        if answer > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return answer + 1
            else:
                q.append((w, answer + 1))

    return answer


print(solution1(begin, target, words))
