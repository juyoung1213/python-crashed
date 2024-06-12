from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (행, 열, 이동 칸 수)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 도착지에 도달했는지 확인
        if x == n-1 and y == m-1:
            return dist
        
        # 현재 위치에서 4 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵을 벗어나지 않고, 벽이 아니며, 방문하지 않은 곳
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    # 도착지에 도달할 수 없는 경우
    return -1
