import argparse
import os
import classification_model
import recipes

def main():
    parser = argparse.ArgumentParser(description="This scrip processes images and return classification results")

    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    
    # Error handling
    image_path = valid_path(args.image_path)

    # Classify image
    predicted_label = classification_model.image_classify(image_path)

    print(predicted_label)
    # TODO: Add some features like meal style

    # Get recipes
    recipes.print_recipes(1, predicted_label)


def valid_path(image_path):
    if not os.path.isfile(image_path):
        raise argparse.ArgumentTypeError(f"The file {image_path} does not exist.")
    if not image_path.lower().endswith(('.png', '.jpeg','.jpg')):
        raise argparse.ArgumentTypeError("File must be a PNG or JPG imgae.")
    return image_path
    

if __name__ == "__main__":
    main()