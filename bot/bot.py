import os
import discord
from discord.ext import commands
from interactions import CommandContext, SlashCommand
from utils.docker_utils import get_docker_status

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        await self.change_presence(activity=discord.Game(name="Handling Slash Commands"))

        channel_id = 1198411010512535653 
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(f'{self.user} has logged in!')
        else:
            print(f"Could not find channel with ID {channel_id}")

    async def dockerstatus(self, ctx: CommandContext):
        docker_status = get_docker_status()
        await ctx.send(f"```{docker_status}```")

def run_bot():
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("Missing DISCORD_TOKEN environment variable.")

    bot = MyBot()
    bot.add_application_command(SlashCommand(bot.dockerstatus, "dockerstatus", "Get Docker status"))
    bot.run(token)

if __name__ == "__main__":
    run_bot()
