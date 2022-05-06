# discordBot
Creating a discordBot with James

# I did not include directions on where to find things like "Server Settings" because Discord changes their UI
# Make sure you check out https://discordpy.readthedocs.io/en/stable/

There are a few steps that need to be taken outside the code.
1: You need to make sure you are an admin on the Discord server you want your bot to live on.
2: Go to https://discord.com/developers/applications and click "New Application"
3: Name your bot something that is helpful and generate your token.  This will be needed for authenticating the bot.
4: On the bot's page, click the slides for Presence Intent and Server Members Intent, locked under Privileged Gateway 
Intents

After the bot is online and hello is tested you need to create roles:
    Go to your server, and click server settings.
    Pick roles and then create the roles you want. I made two. DC Fans and Marvel Fans