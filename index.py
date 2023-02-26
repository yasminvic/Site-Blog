from flask import Flask, render_template

from models.Post import posts

app = Flask(__name__)

#declarando a rota
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

app.run(debug = True, host = '0.0.0.0', port = 5000)