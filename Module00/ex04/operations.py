# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 07:54:40 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 19:56:30 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
    num = sys.argv[1::]
    if num[0].isdigit() == True and num[1].isdigit() == True:
        a = int(num[0])
        b = int(num[1])
        print("Sum:       ",a + b)
        print("Difference:",a - b)
        print("Product:   ",a * b)
        if b == 0:
            print("Quotient:   ERROR (division by zero)")
            print("Remainder:  ERROR (modulo by zero)")
        else :
            print("Quotient:  ",a / b)
            print("Remainder: ",a % b)
    else :
        print("AssertionError: only integers")
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments")
else:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")