# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 19:24:07 by dacortes          #+#    #+#              #
#    Updated: 2023/03/16 21:49:42 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''import time

def decorador_log(func):
    def decorador_funcion(*args, **kwargs):
        with open("fichero.log", 'a') as opened_file:
            output = func(*args, **kwargs)
            opened_file.write(f"{output}\n")
    return decorador_funcion
    

@decorador_log
def suma(a, b):
    return a + b

@decorador_log
def resta(a, b):
    return a - b

@decorador_log
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)
inicio = time.time()
suma(5,6)
time.sleep(1)
fin = time.time()
print(fin-inicio)'''
class MiGestor:
    def __enter__(self):
        print("Entra en __enter__")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Entra en __exit__")

with MiGestor() as f:
    print("Hola")
def suma(a, b):
    return a + b