citations = [0, 0, 1, 1]

#나의 풀이
answer = 0
count = sorted(citations, reverse=True)

for i in range(max(count), 0, -1):
    k1 = len(list(c for c in citations if c >= i))
    k2 = len(list(cc for cc in citations if cc < i))
    if k1 >= i >= k2:
        answer = i
        break
print(answer)

#다른 풀이 1
def solution(citations):
    citations.sort(reverse=True)
    answer2 = max(map(min, enumerate(citations, start=1)))
    return answer2

print("Another Solution Using enumrate : {}".format(solution(citations)))
