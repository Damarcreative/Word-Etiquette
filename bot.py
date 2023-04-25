import discord
#import os

intents = discord.Intents().all()
client = discord.Client(intents=intents)

sensitive_words = ["word_sensitive1", "word_sensitive2", "f*ck"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    for word in sensitive_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, Your message has been deleted because it contains sensitive words.")
            return

#client.run(os.getenv(API_KEY))
client.run("API_KEY_DISCORD")
