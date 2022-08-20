from discord.ext import commands
import discord
import os
import requests
import json
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="*", intents=intents)

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')



def get_text_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    text_quote = '```' + json_data[0]['q'] + "\n ~" + json_data[0]['a'] + '```'
    return text_quote

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = '**'+json_data[0]['q']+'**' + "\n" + '*'+json_data[0]['a']+'*'
    return quote


@bot.event
async def on_ready():
	print("Manganese is on, user: {0.user}".format(bot))

@bot.command(aliases=['z'])
async def zen(ctx):
    zenquote = get_quote()
    print(zenquote)
    await ctx.channel.send(zenquote)

@bot.command(aliases=['zt'])
async def zentext(ctx):
    zen_text_quote = get_text_quote()
    print(zen_text_quote)
    await ctx.channel.send(zen_text_quote)

@bot.command(aliases=['ping','l'])
async def latency(ctx):
    msg = f"PINGED: {round(bot.latency * 1000)}ms"
    print(msg)
    await ctx.channel.send(msg)

bot.run(TOKEN)
