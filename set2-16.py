n=int(input())
f,c,t=0,0,0
l=list(map(int,input().split()))
for i in range(max(l)):
    for j in l:
        if(j>=i+1):
            f=f+1
            if (i+1 not in l):
                t=t+1
                c=f
                break
if(t==0):
    print(f)
elif(t!=0):
    print(c)
