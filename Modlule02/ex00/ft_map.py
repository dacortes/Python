# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 11:37:41 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 12:07:46 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Implementation of ft_rmap
def ft_map(function_to_appl, iterable):
    for item in iterable:
        yield function_to_appl(item)
