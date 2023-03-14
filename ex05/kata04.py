# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 09:34:01 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 12:18:20 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
result = "module_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}".format(kata[0], kata[1], round(kata[2], 2), kata[3], kata[4])
print(result)