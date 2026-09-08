def numberOfItems(s, startIndices, endIndices):
    n = len(s)
    prefix = [0] * n
    count = 0
    for i in range(n):
        if s[i] == '*':
            count +=1
        prefix[i] = count
    result = []
    left = [-1] * n
    leftx= -1
    for i in range(n):
        if s[i] == '|':
            leftx = i
        left[i] = leftx
    right = [-1] * n
    rightx = -1
    for i in range(n-1,-1,-1):
        if s[i] =='|':
            rightx = i
        right[i] = rightx

    for start , end in zip(startIndices,endIndices):
        start -= 1
        end -=1
        l = right[start]
        r = left[end]
        if l >-1 and r > -1 and l<r:
            result.append(prefix[r]-prefix[l])
        else:
            result.append(0)
    return result

s = "|**|*|*"
startIndices = [1, 1]
endIndices   = [5, 6]
result = numberOfItems(s,startIndices=startIndices,endIndices=endIndices)
print(result)



# Items in Containers:
# '*' = item, '|' = container boundary.
# For each query, find the first '|' from the left and the last '|' from the right.
# Use prefix sum to count '*' between those boundaries.
# Precompute nearest left/right '|' to answer each query in O(1).
# Overall: O(n + q) time, O(n) space.