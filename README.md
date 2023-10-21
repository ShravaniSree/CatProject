# Cats API

## Setup

- This project requires python3.11 or higher.
- To install the requirements, please run `python -m pip install -r requirements.txt`
- To run the app, use `python app.py`
- Base url is, `http://localhost:5000`
- Swagger url, `http://localhost:5000/swagger`
- Note that, the `id` used in this project is the name of the image file (without extension), creating two images with same name is not supported.
- Please refer to the swagger url for understanding more about the different endpoints.

## Run using Docker

- Run `docker build -t cats .` to create image.
- Run `docker run -p 5000:5000 cats` to run container.