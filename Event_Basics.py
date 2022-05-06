import discord
from discord import member

intents = discord.Intents.all()
# This allows communication with the discord program
bot = discord.Client(intents=intents)


# @Is a decorator for the async function
# on_ready() is the even that lets me know the bot is online
# async allows for code to be out of functioning order
# Side note: I am unclear as to why PyCharm wants two rows between this comment and the code


@bot.event
async def on_ready():
    print("BOT IS ONLINE")


# This first pulls the user's name into the variable "username"
# The if statement makes sure the user is not the bot
# The else if is looking for the "hello" input from the user to act. Once it receives "hello" the bot replies
@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            await msg.channel.send(f"Hello, {username}")


@bot.event
async def on_member_join(member):
    guild = member.guild
    guild_name = guild.name
    dm_channel = await member.create_dm()
    await dm_channel.send(f"Welcome to {guild_name}!")


# Do not use the on_reaction_add() because it will not pull from cached events, only events when bot is online
# on_raw_reaction_add() will pull from cache and react to events that happened while offline
# Review https://discordpy.readthedocs.io/en/stable/api.html?highlight=raw%20reaction%20add#discord.on_raw_reaction_add
# to see the payload attributes
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)

    if emoji == "🕸️" and message_id == 972118787413377046:
        role = discord.utils.get(guild.roles, name="Marvel Fan")
        await member.add_roles(role)

    if emoji == "🦇" and message_id == 972118830354681967:
        role = discord.utils.get(guild.roles, name="DC Fan")
        await member.add_roles(role)

# This is the authentication token for my bot
# Once run this will bring the bot online
# ***I am going to try a simple fix for right now until I figure out how to do this correctly.  I will be adding pound
# signs to the token when I upload to GitHub so Discord stops resetting my token.***
bot.run("#####OTcwNzI4MTEyOTkwMDg5MjQ2.Go5-00.M3PN8gOJlSW95RfKxBry_lNZyFW5AFmo0omy6k")
