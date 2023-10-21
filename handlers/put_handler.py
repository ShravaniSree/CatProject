from utils import get_error_response,allowed_file

def update_pic(db_helper,table,request,id):
    cat = db_helper.get(table,False,id)
    
    
    if not cat:
        return get_error_response(404)

    if not request.files:
        return get_error_response(400,"No image provided")

    file = request.files['file']

    if not file:
        return get_error_response(400,"No image provided")

    if allowed_file(file.filename):
        file_data = file.read()
        cat.picture_data = file_data
        db_helper.db.session.commit()
        return "Cat picture updated successfully"
    else:
        return get_error_response(400,"Invalid file type received")