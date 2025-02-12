age=int(input("enter your age : "))
ticket=0

if age >=12:
   ticket=12
   print("the price of the ticket is " , ticket , "$")
elif age>=14:
   ticket=14
   print("the ticket is " , ticket , "$")
elif age >=18:
   ticket=18
   print("the ticket is " , ticket , "$")
else:
   print("no ticket available for this age")

