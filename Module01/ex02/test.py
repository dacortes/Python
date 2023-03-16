# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 22:01:48 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 10:55:03 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

v1 = Vector([[1, 2, 3]])
v2 = Vector([[1], [2], [3]])

print(v1)
print(v1.shape)
print(v2)
print(v2.shape)

v_sum = v1 + v2
print(v_sum)

v_sub = v1 - v2
print(v_sub)

v_scalar = v1 * 2
print(v_scalar)

v_mult = v1 * v2
print(v_mult)