# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 21:57:43 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 10:39:29 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 2 :
    num = sys.argv[1::]
    if num[0].isdigit() == True:
        n = int(num[0])
        if n == 0 :
            print("I'm Zero")
        elif n % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    else :
        print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2 :
    print("AssertionError: more than one argument are provided")
else :
    exit