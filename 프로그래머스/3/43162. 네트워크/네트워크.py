def solution(n, computers):
    dist = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j or computers[i][j] == 1:
                dist[i][j] = 1
            else:
                dist[i][j] = float('inf')
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            network_count += 1
            for j in range(n):
                if dist[i][j] < float('inf'):
                    visited[j] = True
    
    return network_count
