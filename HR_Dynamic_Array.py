n,queries = map(int, input().split(" "))
l1 = [[] for i in range(n)]
lastAnswer = 0
for _ in range(queries):
    q,x,y = map(int, input().split(" "))
    if q == 1:
        idx = ((x^lastAnswer)%n)
        l1[idx].append(y)
    else:
        idx1 = (x ^ lastAnswer)%n
        lastAnswer = l1[idx1][y%len(l1[idx1])]
        print(lastAnswer)
