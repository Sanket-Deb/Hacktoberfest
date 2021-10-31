for t in range(int(input())):
    x,r,m=map(int,input().split())
    #x - max energy
    #r - time of run
    #m - max time req
    if r>m:
        print("NO")
    else:
        print("YES")
