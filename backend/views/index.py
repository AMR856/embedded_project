from flask import jsonify, request
from . import app_views
from typing import Dict, Any
from helpers import handle_bash_command
import os

@app_views.route('/verfiy', methods=['POST'], strict_slashes=False)
def compile_code():
    data: Dict[Any] = request.get_json()
    code: str = data.get('code')
    if not code:
        return jsonify({'err': 'Code wasn\'t found within the body'}), 400
    arduino_board: str = data.get('board')
    if arduino_board:
        arduino_board = 'arduino:avr:' + arduino_board
    else:
        arduino_board = arduino_board + 'uno'
    script_dest: str = os.getenv('SCRIPT_DEST')
    code = code.replace('\"', '\\"')
    try:
        with open(script_dest, 'w') as file:
            file.write(code)
    except FileNotFoundError as _:
        return jsonify({'err': 'Error happened while overwriting the sketch content'}), 500
    sketch_path: str = os.getenv('SKETCH_PATH')
    compile_code_cmd: str = f"arduino-cli compile --fqbn {arduino_board} {sketch_path}"
    status = handle_bash_command(compile_code_cmd)
    if not status:
        return jsonify({'err': 'Error happened while compeiling the code'}), 500
    return jsonify({'msg': 'Compiled code successfully'}), 200

@app_views.route('/upload', methods=['POST'], strict_slashes=False)
def upload_code():
    data: Dict[Any] = request.get_json()
    code: str = data.get('code')
    if not code:
        return jsonify({'err': 'Code wasn\'t found within the body'}), 400
    arduino_board: str = data.get('board')
    if arduino_board:
        arduino_board = 'arduino:avr:' + arduino_board
    else:
        arduino_board = arduino_board + 'uno'
    script_dest: str = os.getenv('SCRIPT_DEST')
    try:
        with open(script_dest, 'w') as file:
            file.write(code)
    except FileNotFoundError as _:
        return jsonify({'err': 'Error happened while overwriting the sketch content'}), 500
    port: str = data.get('port')
    if not port:
        port = 'COM1'
    is_found: bool = handle_bash_command('arduino-cli board list', port, arduino_board)
    if not is_found:
        return jsonify({'err': 'There\'s no port and board with this combination connected to the computer'}), 400
    sketch_path: str = os.getenv('SKETCH_PATH')
    upload_code_cmd: str = f"arduino-cli upload -p {port} --fqbn {arduino_board} {sketch_path}"
    status = handle_bash_command(upload_code_cmd)
    if not status:
        return jsonify({'err': 'Error happened while uploading the code'}), 500
    return jsonify({'msg': 'uploaded code successfully'}), 200
