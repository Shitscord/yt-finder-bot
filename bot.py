import discord, tokens, ytsearch, random ,asyncio
from discord.commands import Option

bot = discord.Bot()

async def videoFinder(searchMethod):
    youtube = ytsearch.youtubeSetup(tokens.YOUTUBE)
    if searchMethod == "word":
        searchWord = ytsearch.mitWord()
    elif searchMethod == "file name":
        searchWord = ytsearch.fileExt()
    else:
        searchWord = ytsearch.randomWord()
    notFound = True
    while notFound:
        linkList=ytsearch.idToLink(ytsearch.parseVideoData(youtube, ytsearch.youtubeSearch(youtube, searchWord)))
        if len(linkList) != 0:
            notFound = False
    youtubeLink = linkList[random.randint(0,len(linkList)-1)]
    return(youtubeLink)

@bot.slash_command(guild_ids=None, description="Search for a random video on YouTube.")
async def video(ctx, searchmethod: Option(str, "Choose the search method", choices=["random", "word", "file name"])):
    await ctx.defer()
    messageSend = str(await(videoFinder(searchmethod)))
    await ctx.respond(messageSend)

@bot.event
async def on_ready():
    print("Bot Ready!")

bot.run(tokens.DISCORD)