priorities = [2, 1, 3, 2]
location = 2

from collections import deque


def solution(priorities, location):
    answer = 0

    temp = deque((a, b) for a, b in enumerate(priorities))
    ans = temp[location]

    temper = deque(sorted(priorities, reverse=True))

    ans2 = []
    while temp:
        if temp[0][1] != temper[0]:
            temp.append(temp.popleft())
        elif temp[0][1] == temper[0]:
            ans2.append(temp.popleft())
            temper.popleft()

    answer = ans2.index(ans) + 1

    return answer


print(solution(priorities, location))
