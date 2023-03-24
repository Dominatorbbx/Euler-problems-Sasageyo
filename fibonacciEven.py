init1= 1
init2= 2
nsum=2
for i in range(0,10000):
    sum=init1+init2
    init1=init2
    init2=sum
    if(sum%2==0 and sum<4000000):
        nsum=nsum+sum
print(nsum)
        
        
        
    
    
    