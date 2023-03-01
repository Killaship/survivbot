import discord
from discord.ext import commands, tasks
import os
import requests
import time
import signal
data=open('httplist.py','r+').read() 
exec(data)

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


key=os.getenv('key')
wkey=os.getenv('wkey')

client = discord.Client()#declaring what the client is.

client = commands.Bot(command_prefix = '$')#Makes the bot prefix.
client.remove_command('help')#Removes the auto help command as it can be buggy.

    # https://discord.com/api/oauth2/authorize?client_id=1079242361491693658&permissions=8&scope=applications.commands%20bot

@client.command()
async def explain(ctx):
    embed = discord.Embed(title="Explanation of This:tm:", description="", color=0xFF0000)
    embed.add_field(name="What is this server?", value="This Discord Server is the community area for Surviv Reloaded, open-source server for the defunct online game surviv.io.")
    embed.add_field(name="What is this bot?", value="This bot was made by Killaship to save the hassle of explaining what this is to everyone.")
    embed.add_field(name="What is Surviv Reloaded?", value="It's an open-source server hosting the original client. In other words, it's the original surviv.io, just hosted by a different server. It's not a clone of Surviv.io.")
    embed.add_field(name="Where can I get more info?", value="Check out this link: https://github.com/hsanger/survivreloaded")
    await ctx.send(embed=embed)#sends the embed.


  
@client.command()
@commands.is_owner()
async def shell(ctx,cmd):
   out = os.popen(str(cmd))
   try:
      await ctx.send(str(out.read()))
   except:
      os.system(cmd)


  
@client.command()
async def links(ctx):
    embed = discord.Embed(title="Links", description="", color=0xFF0000)
    embed.add_field(name="Test Server", value="https://taskjourney.org:449/")
    embed.add_field(name="Discord Perma Invite", value="https://discord.gg/K97hwBtwdm")
    embed.add_field(name="Subreddit", value="https://reddit.com/r/survivreloaded")
    embed.add_field(name="Github", value="https://github.com/hsanger/survivreloaded")
    embed.add_field(name="GitLab (archived)", value="https://gitlab.com/hasanger/survivreloaded")
    await ctx.send(embed=embed)





@client.command()
async def help(ctx):
   
  

    embed = discord.Embed(title="help", description="", color=0xFF0000)#Declaring the help command is an embed.

    

    embed.add_field(name="$explain", value="Explains this server and lists FAQ.")

    embed.add_field(name="$links", value="Lists various links related to the project.")

    embed.add_field(name="$serverstatus", value="Checks whether the game server (or at least website) is up.")

    embed.add_field(name="$checkurl", value="Checks the connectivity of any URL.")

    embed.add_field(name="$help", value="This command.")

    embed.add_field(name="Bot GitHub", value="https://github.com/Killaship/survivbot")

    await ctx.send(embed=embed)#sends the embed.


@client.command()
async def serverstatus(ctx):
    code = urlcheck("https://taskjourney.org:449")
    if(code != 200):
        await ctx.send("The server is currently down or unresponsive. The HTTP code sent was: {http}. ({phrase})".format(http=str(code), phrase=httplist[code]))
    else:
        await ctx.send("The server is currently up. (It sent a response code of 200 OK)")
        await ctx.send("If your game is frozen, it's most likely that the client froze or crashed. The game is still relatively unstable, you'll have to reload the game.")


@client.command()
async def checkurl(ctx,site):
    code = urlcheck(site)
    if(code != 200):
        await ctx.send("The server is currently down or unresponsive. The HTTP code sent was: {http}. ({phrase})".format(http=str(code), phrase=httplist[code]))
    else:
        await ctx.send("The server is currently up. (It sent a response code of 200 OK)")

@client.command()
@commands.is_owner()
async def resetbot(ctx):
	await ctx.send("Bot is reloading, please wait a few seconds before sending commands.")
	exit()

def urlcheck(url):
    signal.alarm(TIMEOUT)    
    try:
        r = requests.head(url)
        return r.status_code
    except TimeoutException:
        return 999
        signal.alarm(0)









   
#runs the bot token.
client.run('youshouldputarealtokenhere') # TOKEN HERE
