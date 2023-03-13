# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 21:57:43 by dacortes          #+#    #+#              #
#    Updated: 2023/03/13 22:24:13 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 2 and isinstance(sys.argv[1], int):
    num = sys.argv[1::]
    n = int(num[0])
    if n == 0 :
        print("I'm Zero")
    elif n % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
else :
    exit