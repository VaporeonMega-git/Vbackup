import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

adminperms = [395534835717898252,684836025788530718] #VaporeonMega and Invalid-User Cheese

@bot.event
async def on_ready():
    print("Connected!")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    if int(ctx.author.id) in adminperms:
        await member.kick()

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    if int(ctx.author.id) in adminperms:
        await member.ban()

@bot.command(pass_context=True,aliases=["randomnum","randnum"])
async def randomnumber(ctx, num1: int, num2: int):
    rand = random.randint(num1,num2)
    await ctx.send("Your random number is " + str(rand))

@bot.command(pass_context=True)
async def say(ctx, channel: int, *args: str):
    channel = bot.get_channel(channel)
    await channel.send(" ".join(args))

@bot.command(pass_context=True)
async def send(ctx, dmchannel: int, *args):
    try:
        ctx.author = bot.get_user(dmchannel)
    except Exception:
        await ctx.send("I couldn't find that ID")
    try:
        await ctx.author.send(" ".join(args))
    except Exception:
        await ctx.send("This person isn't DMable by me!")

@send.error
async def send_error(ctx, error):
    if isinstance(error,commands.BadArgument):
        await ctx.send("You need to give me an integer!")

bot.run("")