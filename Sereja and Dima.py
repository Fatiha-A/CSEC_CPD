k=int(input())
    noc=list(map(int, input().split()))
    tot=0
    totd=0
    check=True
    for i in range(k):
        if check == True:
            n=max(noc[0], noc[-1])
            tot+=int(n)
            noc.pop(noc.index(n))
            check=False
        else:
            m=max(noc[0], noc[-1])
            totd+=int(m)
            noc.pop(noc.index(m))
            check=True
    print(tot,   totd)
