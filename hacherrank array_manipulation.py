def funct1(n, q):
    count = 1
    l2=[]
    l1 = [0]*n
    for i in l1:
        for j in range(len(q)):
            while q[j][0]<=count<=q[j][1]:
                i+=q[j][2]
                break
        count += 1
        l2.append(i)
    print(l2)

funct1(5,[[1,3,7],[2,3,7]])
##l1= [0]*5
##print(l1)
