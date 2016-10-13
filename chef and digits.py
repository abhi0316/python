T=input("enter test:")
if (T>=1 and T<=50):
    
    while(T!=0):
        
        
        a=input("enter no:")
        
        f=str(a)
        if (a>=1 and a<=50):
            c=f.count("1")
            d=len(f)
            e=d-c
            if (e==1):
                print "Yes"
            else:

                print "No"

        T=T-1    
        
