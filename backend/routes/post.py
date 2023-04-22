from configs.config import *
from models.post import Post

@app.route('/post', methods=["POST"])
def post():
    data = request.get_json()

    try:
        new = Post(**data)
        db.session.add(new)
        db.session.commit()
        resp = {"result":"OK"}
    except Exception as error:
        resp = {"result":"Error", "details":str(error)}
    
    return jsonify(resp)
