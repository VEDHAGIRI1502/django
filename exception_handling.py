'''import math
vedha=int(input("enter the value1:"))
#akash=int(input("enter the value 2:"))
try:
    c=vedha/10
    print(c)
except ValueError as c:
    print("don't use string value",type(c))'''




'''try:
    a=int(input("num1:"))
    b=input("num2:")
    result=a+b
except TypeError:
    print("should not add string and int")'''
'''
try:
    a = int(input('num1: '))
    b = int(input('num2: '))
except ValueError as e:
    
        print ('should not use string value')
        print("plese use int value")

try:
    result = a / b
except ZeroDivisionError as e:
    print ('should nt use zero')




print(result)'''


try:
    a=int(input('first number:'))
    b=int(input('second number:'))
    c=a/b
    print(c)

except ZeroDivisionError as msg:
    print('dont use zero',msg)
except ValueError:
    print('dont use string and float')
except TypeError as msg:
    print('cant divide string and integer')

finally:
    print('there is no error')
print('way to exit')