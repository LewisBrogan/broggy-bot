from typing import Any
import discord
import os

class MyBot(discord.Client):
    """A custom Discord bot class."""

    async def on_ready(self):
        """Print a message and announce in a specific channel that we have successfully logged in."""
        print(f"We have logged in as {self.user}")

        channel_id = 1198411010512535653
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send('The bot has started up!')
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

    bot = MyBot()
    bot.run(token)

if __name__ == "__main__":
    run_bot()
