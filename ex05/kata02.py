# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 09:33:51 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 11:37:50 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)
str = f"{kata[1]:02}/{kata[2]:02}/{kata[0]:02} {kata[3]:02}:{kata[4]:02}"
print(str)