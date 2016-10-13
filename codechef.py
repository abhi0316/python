a=input("first int:")
b=input("second int:")
c=input("third int:")
d=input("forth int:")
q=[]
if a>b:
    
    x=a-b
    for i in range(0,x+1):
        q.append(b)
        b=b+1
    

    
else:
    
    y=b-a
    for i in range(0,y+1):
        q.append(a)
        a=a+1
        
t=[]
if c>d:
    
    x=a-b
    for i in range(0,x+1):
        t.append(d)
        d=d+1
    

    
else:
    
    y=d-c
    for i in range(0,y+1):
        t.append(c)
        c=c+1
    
count=0

for i in range(0,len(q)):
    
    for j in range(0,len(t)):
        if (q[i]<t[j]):
            count=count+1

print count            

