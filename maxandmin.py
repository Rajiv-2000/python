def maxAndMini(numberList):
  """find max and mini number in a given list"""
  maxnum=numberList[0]
  mininum=numberList[0]
  for i in numberList:
    if i<mininum:
      mininum=i
    elif i>maxnum:
      maxnum=i
  print(maxnum)
  print(mininum)
numberList=[2,3,54,1,23,12,12,14]
maxAndMini(numberList)
print("Maximum number in list is: ")
print("Minimum number in list is: ")
#for loop:
#i=2, maxnumebr=2, if 2>2, else mini=2< 2
#i=3, maxnumber=2, if 2>3, , else 