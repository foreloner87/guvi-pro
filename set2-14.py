def xor_op(x,y,l):
    v=0
    for i in range(x,y+1):
        v= v ^ l[i]
    return v
n,q=input().split()
n,q=int(n),int(q)
if(n>0):
    if(n>1):
        l1,l2=[],[]
        l=list(map(int,input().split()))
        for i in range(q):
            s1,s2=input().split()
            s1,s2=int(s1),int(s2)
            l1.append(s1)
            l2.append(s2)
        for j in range(q):
            print(xor_op(l1[j]-1,l2[j]-1,l))
    if(n==1):
        s=int(input())
        for i in range(q):
            print(s)
else:
    print("Invalid input")
