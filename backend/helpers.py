#!/usr/bin/env python3
from curses.panel import bottom_panel
import os
import subprocess
import json
from typing import Tuple, Union

def load_env(env_path: str) -> None:
    with open(env_path, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            env_name, env_value = line.split('=')
            os.environ[env_name] = env_value

def checking_if_sketch_exist(code_name: str) -> bool:
    dirs_list = os.listdir()
    for dir in dirs_list:
        if dir == code_name:
            return True
    return False

def handle_command(cmd: str) -> Union[Tuple[str, str], bottom_panel]:
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        if cmd == 'arduino-cli board -json list':
            output_json = json.loads(result.stdout)
            for obj in output_json:
                core: str = obj.get('core')
                port: str = obj.get('address')
                return (core, port)
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to create sketch. Exit code: {e.returncode}")
        print("Error Output:", e.stderr)
        return False

    except subprocess.TimeoutExpired:
        print("Script execution timed out")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    return True
