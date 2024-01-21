import discord
import os

from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from utils.docker_utils import get_docker_status

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())
        self.slash = SlashCommand(self, sync_commands=True)

    async def on_ready(self):
        channel_id = 1198411010512535653
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(f'{self.user} has logged in!')
        else:
            print(f"Could not find channel with ID {channel_id}")

def run_bot():
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("Missing DISCORD_TOKEN environment variable.")

    bot = MyBot()

    @bot.slash.slash(name="dockerstatus", description="Get Docker status")
    async def dockerstatus(ctx: SlashContext):
        docker_status = get_docker_status()
        await ctx.send(f"```{docker_status}```")

    bot.run(token)

if __name__ == "__main__":
    run_bot()
