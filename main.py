import random as r
import time as t

table = int(input("Enter the number table you want to practice : "))
print()
t.sleep(1)

number = int(input("Enter the number of questions you want to practice: "))
print()
t.sleep(1)


print()
print("Let's Begin")
print()
print()

score = 0

for i in range (number):
   
   ask = r.randint(1,10)
   question = table * ask

   print("Here is your question : ",table,"*",ask)
   print()
   t.sleep(2)

   answer = int(input("Enter your answer : "))
   print()
   t.sleep(2)


   if answer == question:
        
        print("Your answer is correct that is : ",answer)
        print()
        print()
        print()
        score = score + 1
        t.sleep(2)

   else:
        
        print("Opps! Your answer is not correct")
        print()
        print("Your answer is : ",answer,",But the correct answer is : ",question)
        print()
        print()
        print()
        t.sleep(2)


t.sleep(2)
print("Here is the result")
print()
t.sleep(1)
print("You have answered : ",score,"correct out of",number)
print()
