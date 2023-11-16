import discord
import sys
import os
# Add the parent directory to sys.path to make the 'usr' package available
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from usr.config import BotConfig

from discord.ext import commands, tasks

class WaterBot(commands.Bot):
    def __init__(self, config):
        intents = discord.Intents.default()
        intents.messages = True
        super().__init__(command_prefix='!', intents=intents)

        self.config = config
        self.water_reminder_task = tasks.loop(minutes=self.config.REMINDER_INTERVAL)(self.water_reminder)

    async def water_reminder(self):
        user = await self.fetch_user(self.config.USER_ID)
        channel = await user.create_dm()

        # Delete previous bot messages
        async for message in channel.history(limit=5):
            if message.author == self.user:
                await message.delete()

        # Send reminder
        await channel.send(self.config.MESSAGE)

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.water_reminder_task.start()

    async def on_message(self, message):
        if message.author == self.user: 
            return

        if message.content == 'debug' and isinstance(message.channel, discord.DMChannel):
            await self.water_reminder()

if __name__ == "__main__":
    config = BotConfig()
    bot = WaterBot(config)
    bot.run(config.BOT_TOKEN)
