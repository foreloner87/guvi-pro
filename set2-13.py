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
            print(min(l[(l1[j]-1):(l2[j]-1)]))
    if(n==1):
        s=int(input())
        for j in range(q):
            print(s)
else:
    print("Invalid input")
