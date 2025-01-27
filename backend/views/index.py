from flask import jsonify, request
from . import app_views
from typing import Dict, Any, List
from models.db_storage import DbStorage
from helpers import checking_if_sketch_exist, handle_command
import os

IGNORE_LIST: List[str] = ['hex_files', 'models', 'venv',
                        'views', '__pycache__', '.env',
                        'app.py', 'helpers.py', 'requirements.txt',
                        '.firebase']

@app_views.route('/program', methods=['POST'], strict_slashes=False)
def program_ardunio():
    data: Dict[Any] = request.get_json()
    code_name: str = data.get('filename')
    username: str = data.get('username')
    email: str = data.get('email')
    if not email or not username:
        return jsonify({'err': 'Email or username weren\'t given'}), 400
    is_valid: bool = DbStorage.authenticate_user(email, username)
    if not is_valid:
        return jsonify({'err': 'User is not validated'}), 401
    if not code_name:
        return jsonify({'err': 'Code name\'t provided in the request'}), 400
    is_found: bool = checking_if_sketch_exist(code_name)
    if not is_found:
        return jsonify({'err': 'Code wasn\'t found'}), 400
    core, port = handle_command('arduino-cli board --format json list')
    if not port:
        return jsonify({'err': 'Your Arduino is not connected'}), 400
    status: bool = handle_command(f'arduino-cli upload -p {port} --fqbn {core} --input-file .\\hex_files\\{code_name}.hex')
    if not status:
        return jsonify({'err': 'Error happened while uploading the code'}), 500
    return jsonify({'msg': 'uploaded code successfully'}), 200

@app_views.route('/all-codes', methods=['GET'], strict_slashes=False)
def get_codes():
    dirs_list: List[str] = os.listdir()
    returned_list: List[str] = []
    for dir in dirs_list:
        if dir not in IGNORE_LIST:
            returned_list.append(dir)
    return jsonify(returned_list), 200
