T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    flag = True
    for i in range(2,n-1):
        x = A[i] - A[i-1]
        y = A[i+1] - A[i]
        if 2*x != y and x != 2*y:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')
        # copy code from desciption
