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
    """
        Returns a dictionary of recipes based on provided id. 
        Returns None if the request failed.
    """
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_fixed_num_recipe_ids(num: int, recipes: dict) -> list:
    """
    Returns a list of random recipe ids from recipes dictionary. 
    If the number of meals in recipes are less than num, return a list of all meal ids.
    Returns None if no meal exists in recipes.
    
    Args:
        num: The number of recipe ids to generate.
        recipes: The recipes dictionary

    Example output:
    ['52815', '52811', '52775']
    """
    meal_ls = recipes["meals"]
    # No meal exists in recipes
    if not meal_ls:
        raise ValueError("No meal exists in recipes.")

    total_meal_num = len(meal_ls)
    # When meal numbers are less than num
    if total_meal_num < num:
        random_nums = range(total_meal_num)
    else:
        random_nums = random.sample(range(total_meal_num), num)

    random_ids = []
    for num in random_nums:
        random_ids.append(recipes["meals"][num]["idMeal"])

    return random_ids


def get_recipe_name(id: str) -> str:
    """ 
    Returns the meal name based on the meal id. 
    """
    valid_id(id)
    return get_recipes_by_id(id)["meals"][0]["strMeal"]


def get_recipe_instruction(id: str) -> str:
    """ 
    Returns the meal instruction based on the meal id.
    """
    valid_id(id)
    return get_recipes_by_id(id)["meals"][0]["strInstructions"]


def valid_id(id: str):
    """ 
    Raise an error when the id does not exist. 
    """
    if not get_recipes_by_id(id)["meals"]:
        raise ValueError("The id does not exist.")


def print_recipes(num, label):
    """ 
    Print recipe information, including name and instructions. 
    """
    recipes = get_recipes_by_ingredient(label)
    id_ls = get_fixed_num_recipe_ids(num, recipes)
    for id in id_ls:
        print(get_recipe_name(id))
        print(get_recipe_instruction(id))
        print("\n")