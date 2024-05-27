import discord
from config import TOKEN, MESSAGE

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.check_channels.start()

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return

    async def check_channels(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for channel in self.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    try:
                        await channel.send(MESSAGE)
                        await channel.delete()
                    except Exception as e:
                        print(f'Error deleting channel {channel.name}: {e}')
            await asyncio.sleep(2)

client = MyClient()
client.run(TOKEN)
