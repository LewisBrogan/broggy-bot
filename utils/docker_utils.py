import asyncio
import subprocess

async def get_docker_status():
    try:
        process = await asyncio.create_subprocess_shell(
            "docker ps",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if stdout:
            return stdout.decode()
        else:
            return f"An error occurred: {stderr.decode()}"
    except Exception as e:
        return f"An error occurred: {e}"
