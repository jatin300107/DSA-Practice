import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx]); idx += 1




def spying_on_Beaver(n,p,m,vertices):
    depth = [0]*(n+1)
    for i in range(2,n+1):
        depth[i] = depth[p[i]] + 1
   
    
    skip = vertices[0]
    for v in vertices:
        if depth[v] < depth[skip]:
            skip = v

    chosen = [v for v in vertices if v != skip]
    return ' '.join([str(m - 1)] + [str(v) for v in chosen])

out = []
for _ in range(t):
    n = int(data[idx]); idx += 1
    parents = [0] * 2
    for _ in range(2,n+1):
        i = int(data[idx]); idx += 1
        parents.append(i)
    m = int(data[idx]); idx += 1
    vertices =[]
    for _ in range(m):
        j = int(data[idx]); idx += 1
        vertices.append(j)

    
    out.append(spying_on_Beaver(n, parents, m, vertices))

print('\n'.join(out))


# CF 2257C - Spying on Beaver
#
# Idea:
# Find the dam vertex with the minimum depth from the root and skip it.
# Place cameras for all other dam vertices.
#
# Minimum cameras = m - 1
#
# Why:
# One destination can be left as the baseline; every other possible
# destination needs to be distinguished using a camera.
#
# Complexity: O(n + m) time, O(n) space.