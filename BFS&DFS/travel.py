tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    #1. 그래프 생성
    d = dict()

    for (start, end) in tickets:
        d[start] = d.get(start, []) + [end]

    #2. 시작점 - [끝점] 역순으로 정렬 - 알파벳 오름차순 정렬을 위해서 역순 정렬함
    for r in d.keys():
        d[r].sort(reverse=True)

    #3. DFS 알고리즘으로 path를 만들어준다.
    st = ["ICN"]
    answer = []

    while st:
        top = st[-1]

        if top not in d or len(d[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(d[top][-1])
            d[top].pop()

    answer.reverse()

    return answer

print(solution(tickets))
