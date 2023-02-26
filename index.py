from flask import Flask, render_template, url_for

from models.Post import posts

app = Flask(__name__)

#declarando a rota
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

app.run(debug = True, host = '0.0.0.0', port = 5000)