# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 12:34:32 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 19:20:27 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class ObjectC(object):
    def __init__(self):
        '''
        ...
        '''
        pass
def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    for i, arg in enumerate(args):
        setattr(obj, "var_{}".format(i), arg)
    for key, value in kwargs.items():
        if key == "var_{}".format(i):
            obj = None
            return(obj)
        setattr(obj, key, value)
    return (obj)
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)