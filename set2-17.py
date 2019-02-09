n,k=input().split()
n,k=int(n),int(k)
if(n>0):
    f=0
    if(n!=1):
        l=list(map(int,input().split()))
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if(l[i]+l[j]==k):
                    f+=1
        if(f>0):
            print("yes")
        else:
            print("no")
    elif(n==1):
        if(n==k):
            print("yes")
        else:
            print("no")
else:
    print("Invalid input")
