# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:58:31 by dacortes          #+#    #+#              #
#    Updated: 2023/03/15 19:39:49 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
    #method to check the arguments
    def check(self, arg ,type):
        if isinstance(arg, str) and type == 'name':
            return (True)
        else:
            return (False)
    #method to initialize the class
    def __init__(self, name):
        if self.check(name,'name') == False:
            print("Error")
            exit ()
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    #method to get recipe by name
    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        for recipes in self.recipes_list.values():
            for  recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"No recipe found with name {name}")
        return (None)
    #method to get recipes by types
    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        if recipe_type not in self.recipes_list:
            print(f"No recipes of type {recipe_type}")
            return []
        recipes = self.recipes_list[recipe_type]
        for i in recipes:
            print(i)
        return (recipes)
    #method to add recipe
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print(f"Error: Expected an instance of class Recipe")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()