#this is simple guessing game project

import random

#function to create hint
def checkN(n):
   if n%2==0:
     print("Hint:Number is divisible by 2")  
   elif n%3==0:
      print("Hint:Number is divisible by 3")
   elif n%4==0:
      print("Hint:Number is divisible by 4")   
   elif n%5==0:
      print("Hint:Number is divisible by 5")   
   else:
      print("Hint:Number is an odd number")
      
   return n
         
#function to play game
def play_game():
 n = random.randint(1,99)
 checkN(n)

 guess = int(input("Enter an interger between 1 and 99 "))

# do a loop
 while n !="guess" :
   if guess < n:
     print("Your guess is lower")
     guess = int(input("Enter an interger between 1 and 99 "))
   elif guess > n:
     print ("guess is high")
     guess = int(input("Enter an interger between 1 and 99 "))
   else:
      print("you are right!!")
      break
   print


def main():  
   play_game()
   while True:
      while True:
         ans= input('Run again? (y/n) ')
         if ans in ('y','n'):
            break
         print('Type either y or n')
      if ans =='y':
         play_game()
      else:
         print('See you Again!!')
         break

main()

