# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 11:17:43 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 12:07:11 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Implementation of ft_filter
def ft_filter(function_to_appl, iterable):
    for item in iterable:
        if function_to_appl(item):
            yield item