from utils import get_error_response

def delete_pic(db_helper,table,id):
    cat = db_helper.get(table,False,id)
    
    if not cat:
        return get_error_response(404)
    
    response  = db_helper.delete(cat)
    if response == True:
        return "Cat picture deleted successfully"
    else:
        return get_error_response(500,"Error Deleting image")