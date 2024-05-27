const { Client } = require('discord.js-selfbot-v13');
const client = new Client();

// Replace 'your_token_here' with your actual token
const token = "your_token_here";

client.on('ready', async () => {
    console.log(`Bot is online: ${client.user.tag}`);
    setInterval(async () => {
        client.channels.cache.forEach(async (channel) => {
            if (channel.type == 'GROUP_DM') {
                try {
                    // Send a notification message
                    await channel.send('Group DMs are not permitted without authorization. ❌');
                    // Delete the group DM
                    await channel.delete();
                } catch (error) {
                    console.error(error);
                }
            }
        });
    }, 2000); // Check every 2 seconds
});

client.login(token);
