#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # for each key in recipe dictionary, check:
    # 1. if it exists
    # 2. if there is enough amount
    # 3. if there is enough amount, how many batches we can do
    # if no ingredient or not enough amount, return 0
    # if there is enough amount, return the number of batches. There can be many batch amounts per ingredients, we return the smallest one (i.e. no use of having 2 batches of butter if we only have 1 for sugar)
    lowest_proportion = []
    try:
        for k in recipe:
            if recipe[k] > ingredients[k]:
                return 0
            else:
                proportion = math.floor(ingredients[k] / recipe[k])
                lowest_proportion.append(proportion)
        return min(lowest_proportion)
    except KeyError:
        return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}

print(recipe_batches(recipe, ingredients))
