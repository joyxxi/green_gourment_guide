import argparse
import os
import classification_model
import recipes

def main():
    # Argument parse
    parser = argparse.ArgumentParser(description="This scrip processes images and return classification results")

    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    
    # Error handling
    image_path = valid_path(args.image_path)

    # Classify image
    predicted_label = classification_model.image_classify(image_path)

    print("Predicted Label:", predicted_label)
    print("\n")

    # Get recipes
    recipes.print_recipes(3, predicted_label)


def valid_path(image_path):
    """
    This function verify the image path. Raise error when the path doesn't exist or the it is not an image file.
    """
    if not os.path.isfile(image_path):
        raise argparse.ArgumentTypeError(f"The file {image_path} does not exist.")
    if not image_path.lower().endswith(('.png', '.jpeg','.jpg')):
        raise argparse.ArgumentTypeError("File must be a PNG or JPG imgae.")
    return image_path
    

if __name__ == "__main__":
    main()