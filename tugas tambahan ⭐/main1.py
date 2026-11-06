import os
from dotenv import load_dotenv

load_dotenv()  # baca token dari file .env
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

def get_fox_image_url():
    url = "https://randomfox.ca/floof/"
    data = requests.get(url).json()
    return data["image"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def fox(ctx):
    await ctx.send(get_fox_image_url())

    embed = discord.Embed(
        title="🦆 Random Duck",
        description="Berikut bebek acak untukmu!"
    )
    embed.set_image(url=image_url)

    await ctx.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))