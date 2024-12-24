#!/usr/bin/python3
import os
import shutil
import subprocess
from typing import Tuple

def load_env(env_path: str) -> None:
    with open(env_path, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            env_name, env_value = line.split('=')
            os.environ[env_name] = env_value

def delete_sketch_if_exists():
    if os.path.exists(os.getenv('SKETCH_PATH')):
        print(f"Folder '{os.getenv('SKETCH_PATH')}' already exists. Removing it...")
        shutil.rmtree(os.getenv('SKETCH_PATH'))

def handle_bash_command(cmd: str) -> bool:
    try:
        result = subprocess.run(
            ["arduino-cli", '-c', cmd],
            check=True,
            capture_output=True,
            text=True
        )
        print("Sketch created successfully!")
        print("Command Output:", result.stdout)
        return True

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
