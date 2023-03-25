n1=2
n2=3
arr1=[2,3]
factors=[]
primeFlag = 1
userInput = 600851475143
maxprimefactor=0

for i in range(2,userInput):
    if(i * i < userInput):
        if(userInput%i==0):
            factors.append(i)
            print(factors)
    else:
        break

for j in range(0, len(factors) ): 
    for i in range(2,factors[j] ):
        if(factors[j] % i == 0):
            print("not a prime number")
            primeFlag = 0
            break
        primeFlag = 1
    if(primeFlag == 1):
        print("it is a prime number", factors[j])
        maxprimefactor=factors[j]
print(maxprimefactor)