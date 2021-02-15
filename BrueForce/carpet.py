from math import sqrt

brown = 24
yellow = 24


def solution(brown, yellow):
    answer = []
    t1 = 0
    t2 = 0
    total = brown + yellow
    temp = sqrt(total)

    if total % temp == 0:
        answer.append(int(sqrt(total)))
        answer.append(int(sqrt(total)))
    else:
        t1 = int((4-yellow+total+sqrt(brown**2 + 8*brown + 16 - 16*total))/4)
        t2 = total // t1

        answer.append(max(t1, t2))
        answer.append(min(t1, t2))

    print(answer)

    return answer


solution(brown, yellow)
