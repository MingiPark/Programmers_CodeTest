answers = [1,3,2,4,2]

def solution(answers):
    t1 = [1, 2, 3, 4, 5]
    t2 = [2, 1, 2, 3, 2, 4, 2, 5]
    t3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    while len(t1) < len(answers):
        t1 = t1+t1

    temp1 = 0
    for i in range(len(answers)):
        if answers[i] == t1[i]:
            temp1 = temp1 + 1

    while len(t2) < len(answers):
        t2 = t2 + t2

    temp2 = 0
    for j in range(len(answers)):
        if answers[j] == t2[j]:
            temp2 = temp2 + 1

    while len(t3) < len(answers):
        t3 = t3 + t3

    temp3 = 0
    for k in range(len(answers)):
        if answers[k] == t3[k]:
            temp3 = temp3 + 1

    result = [temp1, temp2, temp3]
    ans = max(result)
    answer = []
    a = 1
    for i in result:

        if i == ans:
            answer.append(a)
        a = a + 1

    return answer

#Another Solution
#itertools -> cycle function 반복함수
#enumerate -> 순서대로 숫자 매김 함수 i , j in enumerate(list)
from itertools import cycle

def solution2(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

print(solution(answers))