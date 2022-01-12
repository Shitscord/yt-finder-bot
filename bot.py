from os import link
from discord.ext import commands
import discord, tokens, ytsearch, random, asyncio

Client = discord.Client()
client = commands.Bot(command_prefix="!")

def run_coro(coro, client):
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)

async def videoFinder(message, client):
    async with message.channel.typing():
        youtube = ytsearch.youtubeSetup(tokens.YOUTUBE)
        notFound = True
        while notFound:
            linkList=ytsearch.idToLink(ytsearch.parseVideoData(youtube, ytsearch.youtubeSearch(youtube, ytsearch.randomWord())))
            if len(linkList) != 0:
                notFound = False
        youtubeLink = linkList[random.randint(0,len(linkList)-1)]
    run_coro(message.channel.send(youtubeLink), client)

@client.event
async def on_ready():
    print("Bot Ready!")

@client.event
async def on_message(message):
    if message.content.lower().startswith("!video"):
        await videoFinder(message, client)

client.run(tokens.DISCORD)
