scoville = [1,1,1,10,10]
K = 100

import heapq as hq

def solution(scoville, K):
    answer = 0

    heap = []

    for sc in scoville:
        hq.heappush(heap, sc)

    while heap[0] < K:
        try:
            hq.heappush(heap, hq.heappop(heap) + (hq.heappop(heap)*2))
        except IndexError:
            return -1
        answer += 1

    return answer

print(solution(scoville, K))