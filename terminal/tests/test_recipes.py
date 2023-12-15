import unittest
from unittest.mock import patch
from src import recipes


class TestGetRecipes(unittest.TestCase):
    """ 
    This class tests all functions related to API integration.
    """    
    @patch('src.recipes.requests.get')
    def test_get_recipes_by_ingredient(self, mock_get):
        # Mocking a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "meals": [{"idMeal": "52772", "strMeal": "Chicken Handi"}]
        }

        result = recipes.get_recipes_by_ingredient("Chicken")
        self.assertIsNotNone(result)
        self.assertIn("meals", result)
        self.assertEqual(len(result["meals"]), 1)

    @patch('src.recipes.requests.get')
    def test_get_recipes_by_ingredient_failed(self, mock_get):
        # Mocking a failed API response
        mock_get.return_value.status_code = 404

        result = recipes.get_recipes_by_ingredient("Chicken")
        self.assertIsNone(result)

    @patch('src.recipes.requests.get')
    def test_get_recipes_by_id(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "meals": [{"idMeal": "52772", "strMeal": "Chicken Handi"}]
        }

        result = recipes.get_recipes_by_id("52772")
        self.assertIsNotNone(result)
        self.assertIn("meals", result)
        self.assertEqual(len(result["meals"]), 1)


class TestGetFixedNumRecipeIDs(unittest.TestCase):
    """
    This class tests various scenarios for the function get_fixed_num_recipe_ids()
    """
    def test_valid_input(self):
        input = {"meals": [{"idMeal": "52815"}, {"idMeal": "52811"}, {"idMeal": "52775"}]}
        result = recipes.get_fixed_num_recipe_ids(2, input)
        self.assertEqual(len(result), 2)

    def test_num_greater_than_meals(self):
        input = {"meals": [{"idMeal": "52815"}, {"idMeal": "52811"}]}
        result = recipes.get_fixed_num_recipe_ids(5, input)
        self.assertEqual(len(result), 2)

    def test_empty_meals(self):
        input = {"meals": None}
        with self.assertRaises(ValueError):
         recipes.get_fixed_num_recipe_ids(3, input)


class TestGetRecipeDetail(unittest.TestCase):
    """
    This class tests all functions related to get specific details of the recipes.
    """
    @patch('src.recipes.get_recipes_by_id')
    def test_valid_id(self, mock_get_recipes_by_id):
        mock_get_recipes_by_id.return_value = {"meals": None}
        with self.assertRaises(ValueError):
            recipes.valid_id("invalid_id")

    @patch('src.recipes.get_recipes_by_id')
    def test_get_recipe_name(self, mock_get_recipes_by_id):
        mock_get_recipes_by_id.return_value = {"meals": [{"idMeal": "52815", "strMeal": "Chicken Parmesan"}]}
        result = recipes.get_recipe_name("52815")
        self.assertEqual(result, "Chicken Parmesan")

    @patch('src.recipes.get_recipes_by_id')
    def test_get_recipe_instruction(self, mock_get_recipes_by_id):
        mock_get_recipes_by_id.return_value = {"meals": [{"idMeal": "52815", "strMeal": "Chicken Parmesan", "strInstructions": "Here is the instruction."}]}
        result = recipes.get_recipe_instruction("52815")
        self.assertEqual(result, "Here is the instruction.")


if __name__ == '__main__':
    unittest.main()