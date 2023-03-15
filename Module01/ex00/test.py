# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 14:56:30 by dacortes          #+#    #+#              #
#    Updated: 2023/03/15 19:40:05 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
from datetime import datetime
from recipe import Recipe
from book import Book

class TestBookMethods(unittest.TestCase):

    def setUp(self):
        self.book = Book("Cookbook")

        recipe1 = Recipe("Spaghetti Carbonara", 2, 30, ["pasta", "eggs", "bacon", "cheese"], "A classic Italian dish", "lunch")
        recipe2 = Recipe("Tiramisu", 1, 45, ["coffee", "sugar", "eggs", "mascarpone", "ladyfingers"], "A traditional Italian dessert", "dessert")
        recipe3 = Recipe("Caprese Salad", 1, 15, ["tomatoes", "mozzarella", "basil", "olive oil", "salt"], "A simple and fresh salad", "starter")

        self.book.add_recipe(recipe1)
        self.book.add_recipe(recipe2)
        self.book.add_recipe(recipe3)

    def test_get_recipe_by_name(self):
        # Test for existing recipe
        recipe = self.book.get_recipe_by_name("Tiramisu")
        self.assertEqual(recipe.name, "Tiramisu")

        # Test for non-existing recipe
        recipe = self.book.get_recipe_by_name("Risotto")
        self.assertIsNone(recipe)

    def test_get_recipes_by_types(self):
        # Test for existing type of recipe
        recipes = self.book.get_recipes_by_types("lunch")
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, "Spaghetti Carbonara")

        # Test for non-existing type of recipe
        recipes = self.book.get_recipes_by_types("snack")
        self.assertEqual(len(recipes), 0)

if __name__ == '__main__':
    unittest.main()
