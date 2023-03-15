# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 21:57:53 by dacortes          #+#    #+#              #
#    Updated: 2023/03/13 21:58:01 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

list = sys.argv[1:]
if list:
    tmp = ' '.join(list[::1])
    swap = tmp.swapcase()
    print(swap[::-1])
else :
    exit
