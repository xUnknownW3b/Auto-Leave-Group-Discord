import discord, asyncio

client = discord.Client()
token = "your-token-here" 
cmd_prefix = "+"
cmd_name = "antigroup"
farewell_message = "GoodBye Everyone"

@client.event
async def on_ready():
    print("Token verified! Use " + cmd_prefix + cmd_name + " in any chat to use the AntiGroup.") # Confirm script is active

@client.event
async def on_message(msg):
    if msg.author == client.user:
        parts = msg.content.split(' ')
        if parts[0] == cmd_prefix + cmd_name:
            await msg.delete()
            left_count = 0
            for priv_channel in client.private_channels:
                if isinstance(priv_channel, discord.GroupChannel):
                    if priv_channel.id != msg.channel.id: # Skip if the message is in the same group chat
                        left_count += 1
                        await priv_channel.send(farewell_message)
                        await priv_channel.leave()
                        print("Exited group: " + str(priv_channel.id)) # Log the group ID
            await msg.channel.send("``Left [" + str(left_count) + "] group chats!``")
            await client.close() # Close the client after processing


client.run(token, bot=False)
input("Press Enter to exit") # Pause to allow user to read output
