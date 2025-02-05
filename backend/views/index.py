from flask import jsonify
from . import app_views
from helpers import handle_command

@app_views.route('/program', methods=['GET'], strict_slashes=False)
def program_ardunio():
    # return jsonify({"msg": "Task was completed"}), 200
    core, port = handle_command('arduino-cli board --format json list')
    if not port:
        return jsonify({'err': 'Your Arduino is not connected'}), 400
    status: bool = handle_command(f'arduino-cli upload -p {port} --fqbn {core} --input-file .\\hex_files\\sample_code.ino.with_bootloader.hex')
    if not status:
        return jsonify({'err': 'Error happened while uploading the code'}), 500
    return jsonify({'msg': 'uploaded code successfully'}), 200
