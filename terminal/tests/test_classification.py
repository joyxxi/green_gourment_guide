import unittest
from unittest.mock import patch
from src import classification_model


class TestModel(unittest.TestCase):
    """
    This class tests the functionality of image classification."""
    def test_carrot(self):
        result = classification_model.image_classify("/Users/joy/Documents/NEU/courses/5001_Intensive_Foundation/project/green_gourmet_guide/data/images/carrot.png")
        self.assertEqual(result, "carrot")

    def test_corn(self):
        result = classification_model.image_classify("/Users/joy/Documents/NEU/courses/5001_Intensive_Foundation/project/green_gourmet_guide/data/images/corn.jpeg")
        self.assertEqual(result, "corn")