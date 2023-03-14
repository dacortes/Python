# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 18:00:34 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 20:50:54 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if len(sys.argv) == 3:
    arg = sys.argv[1::]
    if isinstance(arg[0], str) == True and arg[1].isdigit() == True:
        str = arg[0]
        num = int(arg[1])
        tmp = re.sub("[^a-zA-Z\s]", "", str)
        parse = tmp.split(" ")
        j = 0
        res = []
        while j < len(parse):
            if len(parse[j]) >= num:
                res.append(parse[j])
                j += 1
            else:
                j += 1
        print(res)
    else :
        print("ERROR")
elif len(sys.argv) > 3:
    print("ERROR")
else:
    print("ERROR")