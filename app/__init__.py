from flask import Flask, jsonify, request, Blueprint
from config import Config
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)


from app import routes
