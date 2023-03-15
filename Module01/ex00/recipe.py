# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:59:15 by dacortes          #+#    #+#              #
#    Updated: 2023/03/15 16:48:37 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#class test
class Recipe:
    #method to check the arguments
    def check(self, arg ,type):
        if isinstance(arg, str) and type == 'name':
            return (True)
        elif isinstance(arg, int) and type == 'cooking_lvl':
            return (True)
        elif isinstance(arg, int) and type == 'cooking_time':
            return (True)
        elif isinstance(arg, list) and type == 'ingredients':
            return (True)
        elif isinstance(arg, str) and type == 'description':
            return (True)
        elif isinstance(arg, str) and type == 'recipe_type':
            return (True)
        else:
            return (False)
    #method to initialize the class
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not self.check(name, 'name'):
            print("Error: name should be a string")
            exit ()
        if not self.check(cooking_lvl, 'cooking_lvl'):
            print("Error: cooking_lvl should be an integer")
            exit ()
        if not self.check(cooking_time, 'cooking_time'):
            print("Error: cooking_time should be an integer")
            exit ()
        if not self.check(ingredients, 'ingredients'):
            print("Error: ingredients should be a list")
            exit ()
        if not self.check(description, 'description'):
            print("Error: description should be a string")
            exit ()
        if not self.check(recipe_type, 'recipe_type'):
            print("Error: recipe_type should be a string")
            exit ()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        pass
    #method to print the content of the class
    def __str__(self):
        txt = ""
        tmp = []
        tmp.append(self.name)
        tmp.append(self.cooking_lvl)
        tmp.append(self.cooking_time)
        tmp.append(self.ingredients)
        tmp.append(self.description)
        tmp.append(self.recipe_type)
        txt = ", ".join(str(i) for i in tmp)
        return (txt)
