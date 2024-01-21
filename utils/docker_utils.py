import subprocess

def get_docker_status():
    try:
        return subprocess.check_output(["docker", "ps"], text=True)
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
