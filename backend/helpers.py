#!/usr/bin/env python3
import os
import subprocess
import json
from typing import Tuple, Union, Any, Dict

def load_env(env_path: str) -> None:
    with open(env_path, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            env_name, env_value = line.split('=')
            os.environ[env_name] = env_value

def handle_command(cmd: str) -> Union[Tuple[str, str], Tuple[bool, None]]:
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )

        if cmd == 'arduino-cli board --format json list':
            try:
                data: Dict[Any, Any] = json.loads(result.stdout)

                for port_obj in data.get('detected_ports', []):
                    matching_boards = port_obj.get('matching_boards', [])
                    if matching_boards:
                        core = matching_boards[0].get('fqbn', '')
                        port = port_obj.get('port', {}).get('address', '')
                        return core, port

            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON output: {e}")
                return False, None

        return True, None

    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False, None

    except subprocess.TimeoutExpired:
        print("Command execution timed out")
        return False, None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False, None
