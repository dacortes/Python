# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 20:53:39 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 22:26:31 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

numbers={
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'
}
alphabet={
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}
def check_error(morse):
    i = 0
    while i < len(morse):
        if morse[i] == ' ' or morse[i].isdigit() == True or morse[i].isalpha() == True:
            i += 1
        else :
            print("ERROR")
            return (False)
    return (True)
def more_than_two(arg):
    union = None
    if len(arg) > 1:
        union = " ".join(arg)
        return (union)
    union = arg[0]
    return (union)
if len(sys.argv) >= 2:
    arg = sys.argv[1::]
    morse = more_than_two(arg)
    if check_error(morse) == True :
        res = []
        i = 0
        while i < len(morse):
            if morse[i].isdigit() == True:
                res.append(numbers[morse[i]])
            elif morse[i].isalpha() == True:
                res.append(alphabet[morse[i].upper()])
            elif morse[i] == ' ':
                res.append('/')
            i += 1
        print(*res)
    else :
        exit