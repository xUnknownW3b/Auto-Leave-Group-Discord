# main.py

import discord
from discord.ext import tasks
import config  # Import the configuration file

client = discord.Client()

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Task to delete group DMs
@tasks.loop(seconds=2)
async def delete_group_dms():
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            try:
                # Send a message and delete the group DM
                await channel.send(config.MESSAGE)
                await channel.delete()
            except Exception as e:
                print(e)

# Task setup
@delete_group_dms.before_loop
async def before_delete_group_dms():
    await client.wait_until_ready()

# Start the task and run the bot
delete_group_dms.start()
client.run(config.TOKEN)
