# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 22:27:47 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 01:19:17 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def  text_analyzer(txt=None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.'''
    if not txt :
        txt = input("What is the text to analyze?\n")
    elif not isinstance(txt, str):
        print("AssertionError: argument is not a string")
        return
    manyu = sum(1 for c in txt if c.isupper())
    minus = sum(1 for c in txt if c.islower())
    num = sum(1 for c in txt if c.isdigit())
    space = txt.count(' ')
    puntc = len(txt) - space - minus - manyu - num
    resul = len(txt)
    print("The text contains",resul,"character(s):")
    print("-",manyu, "upper letter(s)")
    print("-",minus, "lower letter(s)")
    print("-",puntc, "punctuation mark(s)")
    print("-",space, "space(s)")
if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv) == 1:
        exit
    else:
        print("Error: too many arguments")
