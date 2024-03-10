def factorial(n):
  """check the factorial for a given number"""
  if n<0:
    print("Factorial is Not defined for negative numbers")
  elif n==0:
    return 1
  else:
    a=n
    for i in range(1, n):
      a *= i
    return a
 
n=int(input("Enter a number to find it's factorial: "))
print("Factorial of number is: ", factorial(n))

'''
n=6, 1-5

n *= i
i=1  , a=6*1=6,  
i=2, a=6*2=12
i=3, a=12*3=36
i=4, a=36*4=144
i=5, a=144*5=720
i=6, a=720*6=4320
6*5*4*3*2=720

6*5!, 5*4!
call stack

'''