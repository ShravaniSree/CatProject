class DBHelper:
    def __init__(self,db):
        self.db = db
    
    def get(self,table,isAll=True,id=None):

        if isAll:
            result = [row.id for row in table.query.all()]
        else:
            result = table.query.get(id)
        
        return result
    
    def delete(self,row):
        self.db.session.delete(row)
        self.db.session.commit()
        return True

    def add(self,row):
        self.db.session.add(row)
        self.db.session.commit()

        
        