from utils import allowed_file,get_picture_key,get_error_response

def post_cat_pic(db_helper,table,request):
    if not request.files:
        return get_error_response(400,"No image provided")

    file = request.files['file']

    if not file:
        return get_error_response(400,"No image provided")
    
    filename = file.filename
    id=get_picture_key(filename)
    cat = db_helper.get(table,False,id)
    if cat:
        print("Conflict while adding picture",id)
        return get_error_response(409,f"Picture with the same filename {id} already exists")

    if allowed_file(filename):
        file_data = file.read()
        cat_picture = table(id=id,picture_data=file_data)
        db_helper.add(cat_picture)
        return "Cat picture uploaded successfully"
    else:
        print("unknown filetype received",filename)
        return get_error_response(400,"Invalid file type received")