import discord
from discord.ext import commands, tasks
import os
import requests
import time
import signal
import random
import time


bottoken = open("token.txt","r").readline()
print(bottoken)
print(bottoken.strip())

membercount=0
totalmessages=0 # total number of messages since bot turned on
data=open('httplist.py','r+').read()
exec(data)
leaderboard = []
xp = []
timestamps = []

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler (this is where OSdev IDT knowledge is relatable :p)
    raise TimeoutException

# Change the behavior of SIGALRM to call the timeout handler
signal.signal(signal.SIGALRM, timeout_handler)



key=os.getenv('key')
wkey=os.getenv('wkey')

intents = discord.Intents.default()
intents.members = True

client = discord.Client() #declaring what the client is.

client = commands.Bot(command_prefix = '$', intents=intents)#Makes the bot prefix.
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

@client.event
async def on_ready():
    global timestamps
    global leaderboard
    global xp
    print("========")
    print("current UNIX time is {time}.".format(time=int(time.time())))
    print("========")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('========')
    print("reloading XP, timestamps, and boards")
    with open("board.txt") as file:
        leaderboard = file.read().splitlines()
        leaderboard = [int(i) for i in leaderboard]
        file.close()
    with open("xp.txt") as file:
        xp = file.read().splitlines()
        xp = [int(i) for i in xp]
        file.close()
    with open("time.txt") as file:
        timestamps = file.read().splitlines()
        timestamps = [int(i) for i in timestamps]
        file.close()
    print("done")
    print("========")
    #print(leaderboard)
    #print(xp)
    #print(timestamps)





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
    embed.add_field(name="Bot GitHub", value="https://github.com/Killaship/survivbot")
    await ctx.send(embed=embed)



@client.command()
@commands.is_owner()
async def initleaderboard(ctx):

    global leaderboard
    global xp
    global timestamps

    await ctx.send("Initializing leaderboard, this may take a while.")
    time.sleep(0.5)
    await ctx.send("Counting Members")
    global membercount
    members = ctx.message.guild.members

    for member in members:
        await ctx.send(member.id)
        leaderboard.append(member.id)
        xp.append(0)
        membercount += 1
        time.sleep(.1)
    await ctx.send("Member counting finished")
    for member in members:
        timestamps.append(str(round(time.time())))
    file = open("board.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(leaderboard)):
        file.write(str(leaderboard[i]) + "\n")
    file.close()
    await ctx.send("Leaderboard exported to board.txt")

    file = open("xp.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(xp)):
         file.write(str(xp[i]) + "\n")
    file.close()
    await ctx.send("XP counts exported to xp.txt")

    file = open("time.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(timestamps)):
         file.write(str(timestamps[i]) + "\n")
    file.close()
    await ctx.send("Timestamps set in time.txt")



async def syncboards():
    global leaderboard
    global timestamps
    global xp
    file = open("board.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(leaderboard)):

        file.write(str(leaderboard[i]) + "\n")
    file.close()

    file = open("xp.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(xp)):
         file.write(str(xp[i]) + "\n")
    file.close()

    file = open("time.txt", 'w+') 
    file.truncate(0) # overwrite file
    for i in range(len(timestamps)):
         file.write(str(timestamps[i]) + "\n")
    file.close()



@client.event
async def on_message(message):
    id = message.author.id
    global totalmessages
    incXP = random.randrange(5, 10)
    totalmessages += 1
    
    if id in leaderboard: # If the ID is on the leaderboard...

        index = leaderboard.index(id) # Find where the ID is on the leaderboard
        if(round(time.time()) - timestamps[index] >= 3): # 5 minute delay
            xp[index] += incXP # Increment corresponding xp by between 5 and 10 points
            #print("old timestamp: {time}".format(time=round(time.time())))
            timestamps[index] = round(time.time())
            #print("new timestamp: {time}".format(time=round(time.time())))
            #print("User ID {userid} gained {xpamount}".format(userid=id,xpamount=incXP))

    else: # If user ID isn't in message

        print("User ID {userid} is not on leaderboard. Run $initleaderboard again?".format(userid=id))

        #print("Note: $initleaderboard resets leaderboard, spams, takes a long time.") 
    await syncboards()
    
    await client.process_commands(message) # Lets bot process other commands after event is done
    



@client.command()
async def getxp(ctx): # TODO: Allow getting XP of a specific person
    if ctx.author.id in leaderboard: # If the ID is on the leaderboard...
        index = leaderboard.index(ctx.author.id) # Find where the ID is on the leaderboard
        await ctx.send("<@{id}> has {xp} XP!".format(id=ctx.author.id,xp=xp[index]))   
    else:
        await ctx.send("Error! <@{userid}> is not on the leaderboard. :/".format(userid=ctx.author.id))

@client.command()
async def getleaderboard(ctx):
    global leaderboard
    global xp
    text = []
    indices = sorted(range(len(xp)), key=xp.__getitem__, reverse=True)
    
    for i in range(5):
        user = await client.fetch_user(leaderboard[indices[i]])
        #await ctx.send("#{row}: {user} has {pts} points!".format(row=i+1, user=user, pts=xp[indices[i]]))
        text.append("#{row}: {user} has {pts} points!\n".format(row=i+1, user=user, pts=xp[indices[i]]))
    print(''.join(text))
    
    embed = discord.Embed(title=''.join(text), description="Top 5 XP counts!", color=0xFF0000)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
   
  

    embed = discord.Embed(title="help", description="", color=0xFF0000)#Declaring the help command is an embed.

    

    embed.add_field(name="$explain", value="Explains this server and lists FAQ.")

    embed.add_field(name="$links", value="Lists various links related to the project.")

    embed.add_field(name="$serverstatus", value="Checks whether the game server (or at least website) is up.")

    embed.add_field(name="$getxp", value="This command shows the amount of XP the sender has.")
    
    embed.add_field(name="$getleaderboard", value="This command lists the 5 members of the server with the most XP!.")

    embed.add_field(name="$checkurl", value="Checks the connectivity of any URL.")

    embed.add_field(name="$help", value="This command.")

    embed.add_field(name="Bot GitHub", value="https://github.com/Killaship/survivbot")

    await ctx.send(embed=embed)#sends the embed.


@client.command()
async def serverstatus(ctx):
    code = urlcheck("https://survivreloaded.com/")
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
client.run(bottoken.strip())
