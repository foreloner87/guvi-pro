def adv(x,y,l):
    v=0
    for m in range(x,y+1):
        v=v+l[m]
    return v

n=int(input())
q=int(input())
if(n>0):
    l=[]
    r1=[]
    r2=[]
    for i in range(n):
        st=int(input())
        l.append(st)
    if(n>1):
        for j in range(q):
            s1=int(input())
            s2=int(input())
            r1.append(s1)
            r2.append(s2)
        for k in range(q):
            print( adv((r1[k]-1),(r2[k]-1),l))
    elif(n==1):
        for i in range(q):
            print(st)
else:
    print("Invalid input")
