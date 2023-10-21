from flask import Response

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}


def get_picture_key(filename):
    return filename.split(".")[0]

def get_error_response(status_code,message=None):
    message = message if message else "picture not found"
    response = Response(message,status=status_code)
    return response
