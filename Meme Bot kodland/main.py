import os
from dotenv import load_dotenv

load_dotenv()  # baca token dari file .env
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

def get_random_meme(category):
    if category == "animals":
        memes = ["animal1.jpg", "animal2.jpg", "animal3.jpg"]
    elif category == "programming":
        memes = ["prog1.jpg", "prog2.jpg", "prog3.jpg"]

    return random.choice(memes)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def animals(ctx):
    file_name = get_random_meme("animals")

    with open(f"images/animals/{file_name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send("🐾 Animal Meme", file=picture)

@bot.command()
async def programming(ctx):
    file_name = get_random_meme("programming")

    with open(f"images/programming/{file_name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send("💻 Programming Meme", file=picture)

bot.run(os.getenv("DISCORD_TOKEN"))