import discord
from discord.ext import commands, tasks

USER_ID = 0 # Replace with your Discord user ID
BOT_TOKEN = '' # Replace with your bot token

REMINDER_INTERVAL = 30  # Interval in minutes
MESSAGE = "Don't forget to drink water! 💧" # The message to send
DEBUG_KEYWORD = 'debug'  # The keyword to trigger the debug response

intents = discord.Intents.default()
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(minutes=REMINDER_INTERVAL)
async def water_reminder():
    user = await client.fetch_user(USER_ID)
    channel = await user.create_dm()
    
    # Delete previous bot messages
    async for message in channel.history(limit=5):
        if message.author == client.user:
            await message.delete()
    
    # Send reminder
    await channel.send(MESSAGE)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await water_reminder()
    water_reminder.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == DEBUG_KEYWORD and isinstance(message.channel, discord.DMChannel):
        await water_reminder()

client.run(BOT_TOKEN)