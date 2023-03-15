# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 19:54:53 by dacortes          #+#    #+#              #
#    Updated: 2023/03/15 21:57:53 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    '''
    A class representing the Stark family. Or when bad things happen to good people.
    '''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.first_name = "Stark"
        self.house_words = "Winter is coming"
    def print_house_words(self):
        txt = self.house_words
        print(txt)
    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    '''
    A class representing the Lannister family. The richest and most powerful family in the Seven Kingdoms.
    '''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.first_name = "Lannister"
        self.house_words = "A Lannister always pays his debts"
    def print_house_words(self):
        txt = self.house_words
        print(txt)
    def die(self):
        self.is_alive = False