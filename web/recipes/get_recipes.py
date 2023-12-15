"""This module integretes the TheMealDB API and implements the feature of recipe processing."""

#######################
# Recipes Processing #
#######################

import requests
import random

def get_recipes_by_ingredient(ingredient: str):
    """ 
        Returns a dictionary of recipes based on provided ingredient. 
        Returns None if the request failed.
    """
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)
    #  HTTP status code that the server returns, 200 is the HTTP status code for "OK," 
    #  which means the request was successful, and the server has sent back a valid response.
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_recipes_by_id(id: str):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def get_fixed_num_recipes(num: int, recipes: dict) -> list:
    """
    Returns a list of random recipe ids from recipes dictionary. 
    If the number of meals in recipes are less than num, return a list of all meal ids.
    Returns None if no meal exists in recipes.
    
    Args:
        num: The number of recipe ids to generate.
        recipes: The recipes dictionary

    Example output:
    [
        {
            "strMeal": "French Lentils With Garlic and Thyme",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwwspt1487394060.jpg",
            "idMeal": "52815"
        },
        {
            ......
        }
    ]
    """
    meal_ls = recipes["meals"]
    # No meal exists in recipes
    if not meal_ls:
        return None
        # raise ValueError("No meal exists in recipes.")

    total_meal_num = len(meal_ls)
    # When meal numbers are less than num
    if total_meal_num < num:
        random_nums = range(total_meal_num)
    else:
        random_nums = random.sample(range(total_meal_num), num)

    random_recipes = []
    for num in random_nums:
        random_recipes.append(recipes["meals"][num])

    return random_recipes


def get_recipe_name(id: str) -> str:
    """ Returns the meal name based on the meal id. """
    valid_id(id)
    return get_recipes_by_id(id)["meals"][0]["strMeal"]


def get_recipe_instruction(id: str) -> str:
    """ Returns the meal instruction based on the meal id."""
    valid_id(id)
    return get_recipes_by_id(id)["meals"][0]["strInstructions"]


def valid_id(id: str):
    """ Raise an error when the id does not exist. """
    if not get_recipes_by_id(id)["meals"]:
        raise ValueError("The id does not exist.")


def get_recipe_detail(id: str):
    return get_recipes_by_id(id)["meals"]




