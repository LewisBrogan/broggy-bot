from utils.docker_utils import get_docker_status

async def docker_status_command():
    return await get_docker_status()
