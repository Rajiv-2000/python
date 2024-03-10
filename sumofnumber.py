def sumOfNumbers(N):
  """Add all the integers from 1 to given number N"""

  sum=0
  for i in range(1, N+1):
    sum += i
    return sum

N=int(input("Enter a number: "))
print("sum of numbers to N is: ", sumOfNumbers(N))

