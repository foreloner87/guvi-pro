n=int(input())
if(n>0):
    f=[]
    c=0
    l=list(map(int,input().split()))
    for i in range(1,max(l)+1):
        if(i in l):
            f.append(l.count(i))
    for j in range(0,len(f)):
        c=c+(f[j]*(j+1))
    print(c)
else:
    print("Invalid input")
