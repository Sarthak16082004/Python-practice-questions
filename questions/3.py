"""Given two integer numbers, write a Python code to return their product only if the product
is equal to or lower than 1000. Otherwise, return their sum"""
a=int (input("enter the first integer"))
b=int (input("enter the second integer"))
product=a*b
sum=a+b

if a*b >=1000:
    print("product:",product)
else:
    print("sum:",sum)