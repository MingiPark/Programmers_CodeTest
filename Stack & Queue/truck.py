bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length

    while q:
        answer += 1
        q.pop(0)

        if truck_weights:
            if weight >= sum(q) + truck_weights[0]:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer

print(solution(bridge_length, weight, truck_weights))