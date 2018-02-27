a=[]
for i in range (0,5):
    n =input('enter no')
    a.append(n)
print(a[0])
# for five numbers inputted
for i in range(0,5):
    for n in range(i,4):
        
        if(a[i]>a[n+1]):
            
            c=a[n+1]
            a[n+1]=a[i]
            a[i]=c
print (a)
        
