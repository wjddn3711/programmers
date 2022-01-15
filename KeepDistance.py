from collections import deque
def solution(places):
    answer = []
    for i in range(len(places)):
        answer.append(bfs(places[i]))

    return answer

# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면,
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다
def bfs(places):
    player = []
    for i in range(5):
        for j in range(5):
            if places[i][j]=='P':
                player.append([i,j])
    if len(player) == 0: return 1
    for p in player:
        visited = [[0]*5 for _ in range(5)]
        dist = [[0]*5 for _ in range(5)]
        queue = deque()
        queue.append(p)
        visited[p[0]][p[1]] = True
        dx = [-1,1,0,0] #상하좌우
        dy = [0,0,-1,1]
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                mx = dx[i]+x
                my = dy[i]+y
                if 0<=mx<5 and 0<=my<5 and visited[mx][my]==0:
                    if places[mx][my]=='O':
                        queue.append([mx,my])
                        visited[mx][my]=1
                        dist[mx][my] = dist[x][y]+1
                    if places[mx][my] =='P' and dist[x][y] <=1:
                        return 0
        return 1



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))