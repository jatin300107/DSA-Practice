import sys
data = sys.stdin.buffer.read().split()
idx = 0
t = int(data[idx]); idx += 1
MAXV = 10**6 + 1
cb = [0] * MAXV
cw = [0] * MAXV
out = []
for _ in range(t):
    n = int(data[idx]); m = int(data[idx+1]); k = int(data[idx+2]); idx += 3
    a = list(map(int, data[idx:idx+n])); idx += n
    b = list(map(int, data[idx:idx+m])); idx += m
    for x in b:
        cb[x] += 1
    matches = 0
    count = 0
    for right in range(n):
        x = a[right]
        cw[x] += 1
        if cw[x] <= cb[x]:
            matches += 1
        if right >= m:
            y = a[right - m]
            if cw[y] <= cb[y]:
                matches -= 1
            cw[y] -= 1
        if right >= m - 1 and matches >= k:
            count += 1
    for x in a:
        cw[x] = 0
    for x in b:
        cb[x] = 0
    out.append(count)
print("\n".join(map(str, out)))

#Below is the dict version that gives TLE cuz of expensive dict operations so instead optimised version uses flat Lists 
'''
import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx]);idx+=1

def  Inaccurate_Subsequence_Search(n,m,a,b,k):
    counter_b = {}
    for x in b:
        counter_b[x] = counter_b.get(x,0) + 1
    
    
    count = 0
    left = 0
    wind_count= {}
    matches = 0
    for right in range(n):
        if a[right] in counter_b:
            wind_count[a[right]] = wind_count.get(a[right],0) + 1
            if wind_count[a[right]] <= counter_b[a[right]]:
                matches += 1
        if right-left+1 == m:
            if matches >= k:
                count += 1
            if a[left] in counter_b:
                if wind_count[a[left]] <= counter_b[a[left]]:
                    matches -= 1
                wind_count[a[left]] -= 1
                
            left += 1
    print(count)
for _ in range(t):
    n = int(data[idx]);idx+=1
    m = int(data[idx]);idx+=1
    k = int(data[idx]);idx+=1
    a = []
    b = []
    for _ in range(n):
        v = int(data[idx]);idx+=1
        a.append(v)
    for _ in range(m):
        x = int(data[idx]);idx+=1
        b.append(x)

    Inaccurate_Subsequence_Search(n=n,m=m,a=a,b=b,k=k)'''