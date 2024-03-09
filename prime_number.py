def prime(number):
  """check given number is prime number or not"""
  count = 2
  if number==0:
     return False
  
  for i in range(2, number):
    if number % i == 0:
      count= count+1
    if count>2:
      return False
    else:
      continue
    
  if count==2:
     return True
  
number = int(input("Enter a number: "))

if prime(number):
    print("Yes, it's a prime number")
else:
    print("No, It's not a prime number")

'''
number=5  , 1,5
count=0  i= 2,3,4
 i=2, 5%2!=0, count=0
 i=3, 5%3!=0, count=0
 i=4, 5%4!=0, count=0
 return False

 i=1, 5%1=0, count=1

'''