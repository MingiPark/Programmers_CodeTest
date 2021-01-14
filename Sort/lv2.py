
numbers = [63, 30, 34, 3, 5, 9, 987, 96, 0, 1000]

#내가 푼 풀이 1 - permutation이 비효율적이여서 시간 초과 에러 발생
import itertools
numbers = list(map(str, numbers))
temp = list(map(''.join, itertools.permutations(numbers, len(numbers))))
temp2 = list(map(int, temp))
ans = max(temp2)
answer = str(ans)

#lambda 활용 방법
#x*3을 하는 이유? num의 인수 값이 1000이하이므로 3자리수로 맞춘뒤 비교한다는 의미이다.
#문자열로 변환 뒤 비교하는 것으로 ASCII코드를 비교하게 된다.
#같을 경우 다음 것을 비교한다.
#str(int) 이유 ? 0000의 경우 0으로 출력하려면 int하고 다시 변환해야 한다.

num = list(map(str, numbers))
num.sort(key=lambda x: x*3, reverse=True)
ans2 = str(int(''.join(num)))
print("another sol use lambda : {}".format(ans2))

t1 = '0000'
t2 = str(t1)
t3 = int(t1)
t4 = str(t3)
print("결과 비교 : {0}(str만 적용한 경우) {1}(str(int)의 경우)".format(t2, t4))
