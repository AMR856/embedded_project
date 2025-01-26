#!/usr/bin/env python3
import os
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound, InternalServerError
from views import app_views
from flask_cors import CORS
from models.db_storage import DbStorage
from helpers import load_env

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app)

@app.errorhandler(404)
def not_found(err: NotFound) -> str:
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def not_found(err: InternalServerError) -> str:
    return jsonify({"error": "The server has something weird going on"}), 500

if __name__ == '__main__':
    load_env('./.env')
    host = os.getenv("API_HOST", '0.0.0.0')
    port = os.getenv('API_PORT', 3000)
    DbStorage.connect()
    app.run(host=host, port=port, debug=True)
