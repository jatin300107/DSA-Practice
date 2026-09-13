 
n , m  = map(int,input().split())
tunnel = []
for _ in range(m):
    i , j , x = map(int,input().split())
    tunnel.append([i,j,x])
def highh_score(tunnel,n):
    point = [float('-inf')] * (n+1)
    point[1] = 0
    for _ in range(n):
        for i , j , k in tunnel:
            if point[i] != float('-inf'):
                point[j] = max(point[j] , point[i]+k)
    for _ in range(n):
        for i , j , k in tunnel:
            if point[i] != float('-inf') and point[i] + k > point[j] or point[i] == float('inf'):
                point[j] = float('inf')
    return point[n] if point[n] != float('inf') else -1

result = highh_score(tunnel=tunnel,n=n)
print(result)




