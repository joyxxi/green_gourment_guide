# Green Gourmet Guide Project Structure

This file illustrates the basic structure of the Green Gourmet Guide project.

## Project Directory Structure - Terminal-Based

```bash
terminal/
|
|--- data/
|    |--- images/
|
|--- src/
|    |
|    |--- classification_model.py
|    |
|    |--- recipes.py
|    |
|    |--- main.py
|    |
|    |--- requests_format.txt
|
|--- tests/
```
- **data/**: Contains all the data needed for the project.
    - **images/**: Stores sample images for testing.
- **src/**: Contains all the source code.
    - **classification_model.py/**: Code related to image processing and classification functionality.
    - **recipes.py/**: Code related to recipes processing functionality.
    - **main.py**: The main script that users will run, handling command line interface and integrating all components.
    - **requests_format.txt**: File to illustrate the reponse format from TheMealDB API.
- **tests/**: Contains test cases.

## Directory Structure - Web-Based

```bash
web/
|
|--- image_classifier/
|
|--- recipes/
|
|--- media/
|
|--- web/
|
|--- manage.py
|
|---db.sqlite3
```

- **image_classifier/**: App for functionalities related to image classification.
- **recipes/**: APP for functionalities related to recipes.
- **media/**: Contains all media files uploaded by user.
- **web/**: App for managing the whole project.
- **manage.py**: The main script to manage the project.
- **db.sqlite3/**: Database
The apps are structured according to Django's conventional parttern, with the following elements:
- **migrations/**: Stores migrations for tracking the changes to the models.
- **templates/**: HTML files for the user interface.
- **forms.py**: Handles the upload of files.
- **model.py**: Defines the data structures.
- **views.py**: Connects the models and templates.
- **urls.py**: Contains URL declarations, mapping views to endpoints.