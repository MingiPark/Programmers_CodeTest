#풀이 1
# Counter함수를 이용하여 각 종류별 갯수를 구한다.
# functools의 reduce함수를 이용하여 경우의 수를 계산한다.
# 각 경우에 +1을 해서 곱하는 이유 : ex) 3인 경우에 선택x, 1개선택, 2개선택, 모두 선택과 같이 경우의 수가 4가지이므로
# 마지막에 -1을 하는 이유 : 최소 하나는 선택해야 하므로 모두 선택하지 않은 경우 하나를 빼준다.


from collections import Counter
from functools import reduce

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]

cnt = Counter([kind for name, kind in clothes])
print(cnt)
print(cnt.values())
answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1)-1
print(answer)

#풀이 2
#hash map 사용

def solution(clothes):
    type = {}

    for c,t in clothes:
        if t not in type:
            type[t] = 2
        else:
            type[t] += 1

    count = 1
    for num in type.values():
        count *= num

    return count-1

print("another sol : {}".format(solution(clothes)))
