import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1
s = data[idx]; idx +=1
t = data[idx];  idx+= 1

def maximum_width(n,m,s,t):
    
    left = list(range(m))
    right  = list(range(m))
    forward = 0
    for i in range(n):
        if t[forward] == s[i]:
            left[forward] = i
            forward += 1
            if forward == m:
                break
    backward = m-1
    for i in range(n-1,-1,-1):
        if s[i] == t[backward]:
            right[backward] = i
            backward -= 1
            if backward < 0:
                break
        
    max_width = 1
    for i in range(1,m):
        max_width = max(max_width,right[i]-left[i-1])


    print(max_width)

maximum_width(n,m,s,t)


# CF 1492C Maximum Width
# Claim: width is set by one adjacent pair (t[i], t[i+1]).
# Put the prefix t[0..i] as far left as possible and the suffix
# t[i+1..] as far right as possible. They cannot collide, so the
# pair gives right[i+1] - left[i]. Answer = max over all i.
# Pattern: earliest match from the left + latest match from the right.
# Time O(n), space O(m).
# Mistakes to avoid next time:
# - Mixing up an index into t with a position in s.
# - Restarting an inner scan per i (O(n*m)); use one pointer and never restart.
# - Coding before stating the claim in words.