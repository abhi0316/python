a=raw_input("enter score:")

c=len(a)

d=a.count("1")
if (c>=11):
    if(d==11):
        print "WON"
    else:
        print "LOST"
        
