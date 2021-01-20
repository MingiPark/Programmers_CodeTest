numbers = [1, 1, 1, 1, 1]
target = 3

# bfs 활용 풀이
import collections


def solution1(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    temp = 0
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))
    return answer


print(solution1(numbers, target))

# dfs 활용 풀이
answer2 = 0


def dfs(idx, numbers, target, value):
    global answer2
    N = len(numbers)
    if idx == N and target == value:
        answer2 += 1
        return
    if idx == N:
        return

    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])


def solution2(numbers, target):
    global answer2
    dfs(0, numbers, target, 0)
    return answer2


print(solution2(numbers, target))

#solution 3

from itertools import product
def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution3(numbers, target))