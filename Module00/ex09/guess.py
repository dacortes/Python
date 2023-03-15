# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 23:12:20 by dacortes          #+#    #+#              #
#    Updated: 2023/03/15 11:42:14 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random

#funtion for printing menu
def print_msg():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

#funtion for smallest number
def smallest_num(num):
    print("ff")

#funtion for str to int
def atoi_num(num):
    atoi = 0
    if num.isdigit() == True and num != 'exit':
        if len(num) == 1 or len(num) == 2:
            atoi = int(num)
            return(atoi)
        else :
            print("Error-num: Number out of range")
            return(False)
    elif num.isdigit() == False and num == 'exit':
            return('exit')
    else:
        print("That's not a number.")
        return(False)

#main
guess = random.randint(1,99)
#guess = 42
#print(guess)
if len(sys.argv) == 1:
    print_msg()
    quit = True
    attempts = 1
    while quit:
        num = input("\nWhat's your guess between 1 and 99?\n")
        check = atoi_num(num)
        if check == False:
            quit = True
        elif check == guess and guess != 42:
            print("Congratulations, you've got it!")
            print("You won in", attempts, "attempts")
            quit = False
        elif check == guess and guess == 42:
            print("The answer to the ultimate question",end="")
            print(" of life, the universe and everything is 42.")
            print("Congratulations! You got it on your first try!")
            quit = False
        elif check != 'exit' and check != guess and check > guess:
            print("Too high!")
        elif check != 'exit' and check != guess and check < guess:
            print("Too low!")
        elif check == 'exit':
            print("Goodbye!")
            quit = False
        attempts += 1
