import sys
data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1
tunnel = []
for _ in range(m):
    i = int(data[idx]); idx += 1
    j = int(data[idx]); idx += 1
    x = int(data[idx]); idx += 1
    tunnel.append([i, j, x])
def highh_score(tunnel,n):
    NEG_INF = float('-inf')
    point = [NEG_INF] * (n+1)
   
    point[1] = 0
    for _ in range(n):
        for i , j , k in tunnel:
            if point[i] != NEG_INF:
                point[j] = max(point[j] , point[i]+k)
    INF = float('inf')
    for _ in range(n):
        for i , j , k in tunnel:
            if point[i] != NEG_INF and point[i] + k > point[j] or point[i] == INF:
                point[j] = INF
    return point[n] if point[n] != INF else -1

result = highh_score(tunnel=tunnel,n=n)
print(result)




