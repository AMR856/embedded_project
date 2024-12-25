import subprocess

def handle_bash_command(port: str, board: str) -> bool:
    try:
        result = subprocess.run(
            ["bash", '-c', 'arduino-cli board list'],
            check=True,
            capture_output=True,
            text=True
        )
        output_lines = result.stdout
        for line in output_lines[1:]:
            if port in line and board in line:    
                return True
        return False

    except subprocess.CalledProcessError as e:
        print(f"Failed to list boards. Exit code: {e.returncode}")
        print("Error Output:", e.stderr)
        return False

    except subprocess.TimeoutExpired:
        print("Script execution timed out")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Port         Type              Board Name              FQBN                 Core
# /dev/ttyACM1 Serial Port (USB) Arduino/Genuino MKR1000 arduino:samd:mkr1000 arduino:samd