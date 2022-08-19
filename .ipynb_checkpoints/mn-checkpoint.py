from nextcord.ext import commands
import os
import requests
import json
from dotenv import load_dotenv

client = commands.Bot(command_prefix='*')

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = '**'+json_data[0]['q']+'**' + "\n" + '*'+json_data[0]['a']+'*'
    return quote


@client.event
async def on_ready():
	print("Mangan is on, user: {0.user}".format(client))

@client.command(aliases=['z'])
async def zen(ctx):
    zenquote = get_quote()
    print(zenquote)
    await ctx.channel.send(zenquote)

@client.command(aliases=['ping','l'])
async def latency(ctx):
    await ctx.channel.send(f"PINGED: {round(client.latency * 1000)}ms")

@client.command()
async def pee():
    pass
client.run(TOKEN)
