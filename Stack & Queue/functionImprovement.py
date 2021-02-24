
progresses = [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5, 10, 7]


def solution1(progresses, speeds):
    answer = []
    tt = []
    for i in range(len(progresses)):
        temp = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            temp += 1
        tt.append(temp)

    start = tt[0]
    ans = [0]
    for i in tt:
        if i > start:
            ans.append(tt.index(i))
            start = i
    ans.append(len(tt))

    answer = list(map(lambda a,b : b-a, ans[:], ans[1:]))
    while 0 in answer:
        answer.remove(0)

    return answer

print(solution1(progresses, speeds))

