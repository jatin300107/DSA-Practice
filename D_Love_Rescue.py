# CF939D - Love Rescue
# Tags: DSU
#
# Two strings s, t of same length. A "spell" (c1, c2) lets you swap c1<->c2 
# everywhere in both strings, any number of times. Find min spells so s == t 
# is achievable, and output the spell set.
#
# Approach: union(s[i], t[i]) for every index i -> letters that must become
# interchangeable end up in the same DSU component. A component of size k
# needs exactly k-1 spells (any spanning tree over its letters works -
# problem has a special judge, so the shape of the tree doesn't matter,
# only that it connects the component with min edges).
#
# Bug I hit: find(x) called find(x) instead of find(parent[x]) - infinite
# recursion once parent[x] != x, since x never advances toward the root.

import sys
data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1

s = str(data[idx]);idx +=1

t = str(data[idx]); idx +=1
    



def love_rescue(n,s,t):
    parent = list(range(26))
    
    def find(x):
        if parent[x] != x:
            parent[x]=find(parent[x])
        return parent[x]

    def union(a,b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra
    
    for i in range(n):
        
        union(ord(s[i])-97, ord(t[i])-97)
    spells = []
    for c in range(26):
        root = find(c)
        if c != root:
            spells.append((chr(c + ord('a')), chr(root + ord('a'))))
    print(len(spells))
    for a,b in spells:
        print(f"{a} {b}")


love_rescue(n,s,t)

    
