import os
def load_env(env_path: str) -> None:
    with open(env_path, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            env_name, env_value = line.split('=')
            os.environ[env_name] = env_value
