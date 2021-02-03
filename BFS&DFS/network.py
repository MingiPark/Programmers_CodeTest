n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def dfs(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1
    for e in range(len(computers)):
        if computers[v][e] == 1 and visited[e] == 0:
            dfs(computers, visited, e)

def solution1(n, computers):
    answer = 0
    visited = [0] * n
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(computers, visited, i)
                answer += 1
    return answer

print(solution1(n,computers))