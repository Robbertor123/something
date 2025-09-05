def rex(s):
    v=[s[i:j] for i in range(len(s))for j in range(i+1,len(s)+1)]
    return v
n=int(input())
for i in range(n):
    s,a,b=input().split()
    a,b=int(a),int(b)
    p=rex(s)
    m=0
    for h in p:
        if len(h)>1 and h[0]=='0':
            continue
        f=int(h)
        if a<=f<=b:
            m+=1
    #print(p)
    print(m)
