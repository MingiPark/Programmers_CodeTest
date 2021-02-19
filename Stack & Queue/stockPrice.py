prices = [1, 2, 3, 2, 3, 1]
#5,4,1,2,1,0

#정확성 100% but, 효율설 0%
def solution1(prices):
    answer = []

    for i in range(len(prices)):
        temp = prices[i:-1] + [0]
        print(temp)
        tmp = temp[0]
        k = 0
        ans = 0
        while tmp <= temp[k] and k <= len(temp)-2:
            ans += 1
            k += 1
        answer.append(ans)

    return answer

print(solution1(prices))

