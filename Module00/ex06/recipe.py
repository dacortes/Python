# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 12:21:39 by dacortes          #+#    #+#              #
#    Updated: 2023/03/14 17:58:57 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook= {
    'bocadillo':{
        'ingredients':['jamon', 'pan', 'queso', 'tomate'],
        'meal':['almuerzo'],
        'prep_time':['10']
        },
    'tarta':{
        'ingredients':['harina', 'azucar', 'huevos'],
        'meal':['postre'],
        'prep_time':['60']
        },
    'ensalada':{
        'ingredients':['aguacate', 'rucula', 'espinacas'],
        'meal':['almuerzo'],
        'prep_time':['15']
    }
}
def add_recipe(cookbook, name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time':prep_time
    }
def print_name(cookbook):
    print("List of recipes")
    i = 0
    while i < len(cookbook):
        key = list(cookbook.keys())[i]
        i += 1
        str_i = f"{i}."
        print("  ",str_i,key)
def print_details(cookbook,name):
    if name not in cookbook:
        print("Sorry, this recipe does not exist.")
    else:
        print("\nRecipe for", name,end=":")
        print("\n   Ingredients list:",cookbook[name]['ingredients'])
        print("   To be eaten for",*cookbook[name]['meal'])
        print("   Takes",*cookbook[name]['prep_time'],"minutes of cooking.")
def delete_recipe(cookbook,name):
    print("Recipe to delete")
    if name not in cookbook:
        print("Sorry, this recipe does not exist.")
    else :
        del cookbook[name]
def print_menu():
    print("List of available option:")
    print("      1: Add a recipe")
    print("      2: Delete a recipe")
    print("      3: Print a recipe")
    print("      4: Print the cookbook")
    print("      5: Quit")
    print("\nPlease select an option:")
print("Welcome to the Python Cookbook !")
print_menu()
quit = True
while quit:
    opt = input()
    if opt == '1':
        ingredients =[]
        name = input("Enter a name:\n")
        ingredient = input("Enter ingredients:\n")
        while ingredient:
            ingredients.append(ingredient)
            ingredient = input()
        meal = input("Enter a meal type:\n")
        time = input("Enter a preparation time:\n")
        add_recipe(cookbook,name,ingredients,meal,time)
    elif opt == '2':
        delete_recipe(cookbook,input())
    elif opt == '3':
        print_details(cookbook,input("\nPlease enter a recipe name to get its details:\n"))
    elif opt == '4':
        print_name(cookbook)
    elif opt == '5':
        quit = False
        print("\nCookbook closed. Goodbye !")
        break
    else:
        print("Sorry, this option does not exist.")
    print_menu()