# Green Gourmet Guide Project Structure

This file illustrates the basic structure of the Green Gourmet Guide project.

## Project Directory Structure

green_gourment_guide/
|
|--- data/
|    |--- images/
|
|--- src/
|    |
|    |--- classification_model/
|    |
|    |--- recipes/
|    |
|    |--- main.py
|
|--- tests/
|
|--- STRUCTURE.md


## Directory Descriptions

- **data/**: Contains all the data needed for the project.
    - **images/**: Stores sample images for testing the image recognition model.
    - **models/**: Models for image recognition.
- **src/**: Contains all the source code.
    - **classification_model.py/**: Code related to image imput, processing, and classification functionality.
    - **recipes.py/**: Code related to recipes processing functionality.
    - **main.py**: The main script that users will run, handling command line interface and integrating all components.
- **tests/**: Contains test cases.
- **STRUCTURE.md**: Documentation for illustrating the structure of the project.