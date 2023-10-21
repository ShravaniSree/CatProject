import io
from flask import send_file
from utils import get_error_response

def get_selected(db_helper,table,id):
    cat = db_helper.get(table,False,id)
    if cat:
        return send_file(io.BytesIO(cat.picture_data), mimetype='image/jpeg')
    else:
        return  get_error_response(404)

def get_all(db_helper,table):
    cat_pictures = db_helper.get(table)
    return {"cat_pictures": cat_pictures}