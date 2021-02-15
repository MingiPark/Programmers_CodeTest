numbers = "011"

from itertools import permutations

def prime(num):
    if num != 1 and num != 0:
        for f in range(2, num):
            if num % f == 0:
                return False
    else:
        return False

    return True


def solution(numbers):
    temp = list(numbers)
    temp2 = []
    for i in range(1, len(temp) + 1):
        temp2.append(list(map(''.join, permutations(temp, i))))

    temp2 = sum(temp2, [])
    temp2 = list(set(map(int, temp2)))

    answer = 0

    for j in range(len(temp2)):
        if prime(temp2[j]):
            answer += 1

    return answer

print(solution(numbers))