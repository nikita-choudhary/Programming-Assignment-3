#2.	Write a Python Program to Check if a Number is Odd or Even?
a=int(input("Enter the number : "))
p=a/2
if p==0 and a!=0:
    print(a," is an even number.")
elif p!=0:
    print(a," is an odd number.")
else:
    print(a," is neither even nor odd.")