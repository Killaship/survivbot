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


httplist = []
for i in range(1000):
	httplist.append("Web Server Returned an Unknown Error")
httplist[100] = "Continue"
httplist[101] = "Switching Protocols"
httplist[102] = "Processing"
httplist[103] = "Early Hints"

httplist[200] = "OK"
httplist[201] = "Created"
httplist[202] = "Accepted"
httplist[203] = "Non-Authoritative Information"
httplist[204] = "No Content"
httplist[205] = "Reset Content"
httplist[206] = "Partial Content"
httplist[207] = "Multi-Status"
httplist[208] = "Already Reported"
httplist[226] = "IM used"

httplist[300] = "Multiple Choices"
httplist[301] = "Moved Permanently"
httplist[302] = "Found"
httplist[303] = "See Other"
httplist[304] = "Not Modified"
httplist[305] = "Use Proxy"
httplist[306] = "Switch Proxy"
httplist[307] = "Temporary Redirect"
httplist[308] = "Permanent Redirect"

httplist[400] = "Bad Request"
httplist[401] = "Unauthorized"
httplist[402] = "Payment Required"
httplist[403] = "Forbidden"
httplist[404] = "Not Found"
httplist[405] = "Method Not Allowed"
httplist[406] = "Not Acceptable"
httplist[407] = "Proxy Authentication Required"
httplist[408] = "Request Timeout"
httplist[409] = "Conflict"
httplist[410] = "Gone"
httplist[411] = "Length Required"
httplist[412] = "Precondition Failed"
httplist[413] = "Request Entity Too Large"
httplist[414] = "Request-URI Too Long"
httplist[415] = "Unsupported Media Type"
httplist[416] = "Requested Range Not Satisfiable"
httplist[417] = "Expectation Failed"
httplist[418] = "I'm a teapot"
httplist[421] = "Misdirected Reques"
httplist[422] = "Unprocessable Entity"
httplist[423] = "Locked"
httplist[424] = "Failed Dependency"
httplist[425] = "Too Early"
httplist[426] = "Upgrade Required"
httplist[428] = "Precondition Required"
httplist[429] = "Too Many Requests"
httplist[431] = "Request Header Fields Too Large"
httplist[451] = "Unavailable For Legal Reasons"

httplist[500] = "Internal Server Error"
httplist[501] = "Not Implemented"
httplist[502] = "Bad Gateway"
httplist[503] = "Service Unavailable"
httplist[504] = "Gateway Timeout"
httplist[505] = "HTTP Version Not Supported"
httplist[506] = "Variant Also Negotiates"
httplist[507] = "Insufficient Storage"
httplist[508] = "Loop Detected"
httplist[510] = "Not Extended"
httplist[511] = "Network Authentication Required"

# NON-STANDARD CODES

httplist[419] = "CSRF Token Missing or Expired"
httplist[420] = "Enhance Your Calm"
httplist[440] = "Login Time-out"
httplist[444] = "No Response"
httplist[449] = "Retry With"
httplist[450] = "Blocked by Windows Parental Controls"
httplist[460] = "Client closed the connection with AWS Elastic Load Balancer"
httplist[463] = "The load balancer received an X-Forwarded-For request header with more than 30 IP addresses"
httplist[494] = "Request header too large"
httplist[495] = "SSL Certificate Error"
httplist[496] = "SSL Certificate Required"
httplist[497] = "HTTP Request Sent to HTTPS Port"
httplist[498] = "Invalid Token (Esri)"
httplist[499] = "Client Closed Request"

httplist[520] = "Web Server Returned an Unknown Error"
httplist[521] = "Web Server Is Down"
httplist[522] = "Connection Timed out"
httplist[523] = "Origin Is Unreachable"
httplist[524] = "A Timeout Occurred"
httplist[525] = "SSL Handshake Failed"
httplist[526] = "Invalid SSL Certificate"
httplist[527] = "Railgun Error"
httplist[530] = "Origin DNS Error"
httplist[561] = "Unauthorized (AWS Elastic Load Balancer)"

httplist[609] = "Nice."
httplist[999] = "The connection timed out after 10 seconds. This means the server most likely is down, or it spun out into an infinite loop. (The bot killed urlcheck() after {sec} seconds!)".format(sec=TIMEOUT)


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
