from flask import jsonify, request, abort
from . import app_views
from typing import Dict, Any
from helpers import handle_bash_command
import os

@app_views.route('/verfiy', methods=['POST'], strict_slashes=False)
def compile_code():
    data: Dict[Any] = request.get_json()
    code = data.get('code')
    if not code:
        return jsonify({'err': 'Code wasn\'t found within the body'}), 400
    script_dest: str = os.getenv('SCRIPT_DEST')
    overwrite_file_content_cmd: str = f'echo -e {code} > {script_dest}'
    status = handle_bash_command(overwrite_file_content_cmd)
    if not status:
        return jsonify({'err': 'Error happened while overwriting the sketch content'}), 500
    compile_code_cmd: str = f"arduino-cli compile --fqbn {os.getenv('ARDUINO_BOARD')} {os.getenv('SKETCH_PATH')}"
    status = handle_bash_command(compile_code_cmd)
    if not status:
        return jsonify({'err': 'Error happened while compeiling the code'}), 500
    return jsonify({'msg': 'Compiled code successfully'}), 200
