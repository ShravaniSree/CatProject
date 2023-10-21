import os
import io
from db_helper import DBHelper
from initialize_app import get_app
from flask_cors import CORS
from database import db,CatPicture
from flask import request, jsonify, send_file
from handlers import post_handler,get_handler,put_handler,delete_handler
from utils import allowed_file,get_picture_key,get_error_response
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

app = get_app()
CORS(app)
db.init_app(app)
db_helper = DBHelper(db)

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Cats API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)




@app.route('/upload', methods=['POST'])
def upload_cat_picture():
    result = post_handler.post_cat_pic(db_helper,CatPicture,request)
    return result
    


@app.route('/get', methods=['GET'])
def get_cat_pictures():
    response = get_handler.get_all(db_helper,CatPicture)
    return jsonify(response)


@app.route('/get/<string:id>', methods=['GET'])
def get_cat_picture(id):
    response = get_handler.get_selected(db_helper,CatPicture,id)
    return response
    
    

@app.route('/update/<string:id>', methods=['PUT'])
def update_cat_picture(id):
    response = put_handler.update_pic(db_helper,CatPicture,request,id)
    return response
    


@app.route('/delete/<string:id>', methods=['DELETE'])
def delete_cat_picture(id):
    response = delete_handler.delete_pic(db_helper,CatPicture,id)
    return response



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5000)
