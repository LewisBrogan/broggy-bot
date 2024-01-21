import os
import discord
from discord.ext import commands
from utils.docker_status import get_docker_status

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.tree.add_command(dockerstatus)
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

@discord.app_commands.command(name="dockerstatus", description="Get Docker status")
async def dockerstatus(interaction: discord.Interaction):
    await interaction.response.defer()
    docker_status = await get_docker_status()
    await interaction.followup.send(f"```{docker_status}```")

def run_bot():
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("Missing DISCORD_TOKEN environment variable.")

    bot = MyBot()
    bot.run(token)

if __name__ == "__main__":
    run_bot()
