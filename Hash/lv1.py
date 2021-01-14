participant = ["c", "a", "b", "c"]
completion = ["a", "b", "c"]

#풀이1 : zip을 이용하여 미리 정렬해둔 리스트에서 없는 값을 찾는다.
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par
    return participant[-1]

print(solution(participant, completion))

#풀이 2: collections.Counter를 사용하는 경우 객체들끼리의 뺄셈이 가능하다.
#주의 : 딕셔너리 형식으로 만들어져 list(a.keys())[0]과 같이 표현해야 값을 알 수 있다.
import collections
answer = collections.Counter(participant) - collections.Counter(completion)
print("Another solution use collections.Counter() : {}".format(list(answer.keys())[0]))

#풀이 3: hash를 이용하는 방법
#hash()는 마치 자료들의 주소값처럼 실행될 때마다 각 값에 대한 고유한 정수형 숫자를 반환한다.
#따라서 par의 hash값을 모두 더한뒤 com의 hash값을 빼주면 결과 값의 hash값이 나오게 된다.
temp = 0
ans = 0
dic = {}
for i in participant:
    dic[hash(i)] = i
    temp += hash(i)
for j in completion:
    temp -= hash(j)
ans = dic[temp]
print("3rd Solution Use hash() : {}".format(ans))
