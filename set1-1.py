n=int(input())
if(n!=0):
    l=[]
    ln=[]
    sto=[]
    f,cf=0,0
    for i in range(n):
        s=input()
        l.append(s)
        ln.append(len(s))
    for i in range(min(ln)):
        for j in l:
            if(s[i]==j[i]):
                f+=1
                if(f==n):
                    f=0
                    sto.append(s[i])
                    break
            else:
                f=0
                cf=i
                break
        if(cf):
            break
    s=''.join(sto)
    print(s)
else:
    print("Invalid number")
