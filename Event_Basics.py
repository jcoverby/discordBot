import discord
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


# This is the authentication token for my bot
# Once run this will bring the bot online
bot.run("OTcwNzI4MTEyOTkwMDg5MjQ2.YnALAQ.ABvCv-ghhvWvbJbkZv66pir_UxY")
