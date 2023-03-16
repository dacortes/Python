# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 12:03:48 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 12:07:48 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Implementation of ft_reduce
def ft_reduce(function_to_apply, iterable):
    it = iter(iterable)
    try:
        acc = next(it)
    except StopIteration:
        return None
    for elem in it:
        acc = function_to_apply(acc, elem)
    return acc

