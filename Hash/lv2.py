a = ['119', '976', '119324234234121']
#나의 풀이 - 2중 for문
ans = True
a.sort()
for i in range(len(a)-1):
    l = len(a[i])
    for k in range(i+1, len(a)):
        if a[i][0:l] == a[k][0:l]:
            ans = False

print(ans)

#zip을 이용하여 앞 뒤 값을 비교
#str.startswith()을 이용하여 원하는 문자열 찾기
answer = True
for p1, p2 in zip(a, a[1:]):
    if p2.startswith(p1):
        answer = False
print("Another sol : {}".format(answer))

#hashmap을 사용한 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

solution(a)

