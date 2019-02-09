def adv(x,y,l):
    v=0
    for m in range(x,y+1):
        v=v+l[m]
    return v
n,q=input().split()
n,q=int(n),int(q)
if(n>0):
    r1=[]
    r2=[]
    if(n>1):
        l=list(map(int,input().split()))
        for j in range(q):
            s1,s2=input().split()
            s1,s2=int(s1),int(s2)
            r1.append(s1)
            r2.append(s2)
        for k in range(q):
            print( adv((r1[k]-1),(r2[k]-1),l))
    elif(n==1):
        s=input()
        for i in range(q):
            print(s)
else:
    print("Invalid input")
