n,k = map(int, input().split(" "))
arr = sorted(list(map(int, input().split(" "))))
count =0
try:
    while arr[0]<k:
        count += 1
        sweetness = arr.pop(0)+(2*arr.pop(0))
        arr.insert(0,sweetness)
        arr = sorted(arr)
    print(count)
except:
    print(-1)
