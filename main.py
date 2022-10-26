import random

import logoo

#print header start

print(logoo.logooo)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100 ")

#Enter and check the difficulty

chose = input("Choose a difficulty. Type 'easy' or 'hard' :")

if chose == "easy":

    num = 10

else:

    num = 5

#Random number selection

numberg = random.randint(1,100)

#Enter the number by the user and check it

while (num !=0):

    print(f"you have {num} attempts to guss the number ")

    inp = int(input("Make a guess : "))

    if(inp == numberg):

        print(f" {inp} is a correct number ")

        print(" you are wine ")

        break

    elif(numberg > inp):

        print(f" {inp} too low ")

        num -=1

    elif (numberg < inp):

        print(f" {inp} too high ")

        num -= 1
if(num == 0):
    print(" you are lose ")