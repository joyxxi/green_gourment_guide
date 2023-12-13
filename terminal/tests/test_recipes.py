import unittest
from unittest.mock import patch
from src import recipes

class TestRecipes(unittest.TestCase):
    
    @patch('recipes.requests.get')
    def test_get_recipes_by_ingredient_successful(self, mock_get):
        # Mocking a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "meals": [{"idMeal": "52772", "strMeal": "Chicken Handi"}]
        }

        result = recipes.get_recipes_by_ingredient("Chicken")
        self.assertIsNotNone(result)
        self.assertIn("meals", result)
        self.assertEqual(len(result["meals"]), 1)

    @patch('recipes.requests.get')
    def test_get_recipes_by_ingredient_failed(self, mock_get):
        # Mocking a failed API response
        mock_get.return_value.status_code = 404

        result = recipes.get_recipes_by_ingredient("Chicken")
        self.assertIsNone(result)

    # More tests for other functions...

if __name__ == '__main__':
    unittest.main()

# How to run tests: python -m unittest test_recipes.py