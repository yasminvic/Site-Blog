from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

current_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.dirname(current_path)
database_folder = os.path.join(path, 'database/')
database_file = os.path.join(database_folder, 'data.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_file}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)