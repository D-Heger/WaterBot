import discord
from discord.ext import commands, tasks
import os

class WaterBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        super().__init__(command_prefix='!', intents=intents)

        self.reminder_interval = int(os.environ.get('REMINDER_INTERVAL', 60))  # Default to 60 minutes if not set
        self.user_id = int(os.environ['USER_ID'])  # Raises an error if not set
        self.message = os.environ['MESSAGE']  # Raises an error if not set
        self.water_reminder_task = tasks.loop(minutes=self.reminder_interval)(self.water_reminder)

    async def water_reminder(self):
        user = await self.fetch_user(self.user_id)
        channel = await user.create_dm()

        # Delete previous bot messages
        async for message in channel.history(limit=5):
            if message.author == self.user:
                await message.delete()

        # Send reminder
        await channel.send(self.message)

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.water_reminder_task.start()

    async def on_message(self, message):
        if message.author == self.user: 
            return

        if message.content == 'debug' and isinstance(message.channel, discord.DMChannel):
            await self.water_reminder()

if __name__ == "__main__":
    bot_token = os.environ['BOT_TOKEN']  # Raises an error if not set
    bot = WaterBot()
    bot.run(bot_token)
