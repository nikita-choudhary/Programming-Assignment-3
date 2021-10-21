#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

#prime = True
for i in range(1,10001):
    if i>1:
        for j in range(2,i):
            fact= i%j
            if(fact==0):
                break
    
        else:
            print(i)

   
