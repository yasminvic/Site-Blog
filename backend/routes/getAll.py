from configs.config import *
from models.post import Post

@app.route('/getAll')
def getAll():
    data = db.session.query(Post).all()

    if data:
        data_json = []
        for element in data:
            data_json.append(element.json())
        
        resp = {"result":"OK", "details":data_json}
        return jsonify(resp)
    
    resp = {"result": "OK", "details": "Something got wrong"}
    return jsonify(resp)