def mergeList(A, B):
    C, m, n = [], len(A), len(B)
    i, j = 0, 0
    while i+j < m+n:
        if i == m or A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    return(C)
a = [2,4,6]
b = [1,3,5]
print(mergeList(a,b))

