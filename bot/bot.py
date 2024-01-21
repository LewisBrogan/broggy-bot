from typing import Any
import discord
import os
from discord import Intents

class MyBot(discord.Client):
    """A custom Discord bot class."""

    async def on_ready(self):
        """Print a message indicating that we have successfully logged in."""
        print(f"We have logged in as {self.user}")

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
