from typing import Any
import discord
import os
from discord import Intents

class MyBot(discord.Client):
    """A custom Discord bot class."""

    async def on_ready(self):
        """Announce in a specific channel that the bot has successfully logged in."""
        channel_id = 1198411010512535653
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(f'{self.user} has logged in!')
        else:
            print(f"Could not find channel with ID {channel_id}")

    async def on_message(self, message: discord.Message):
        """Respond to messages starting with '$hello'."""
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

def run_bot():
    """Run the Discord bot."""
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("Missing DISCORD_TOKEN environment variable.")

    intents = Intents.default()
    intents.messages = True

    bot = MyBot(intents=intents)
    bot.run(token)

if __name__ == "__main__":
    run_bot()
