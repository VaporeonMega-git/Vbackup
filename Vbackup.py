import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

adminperms = [395534835717898252,684836025788530718] #VaporeonMega and Invalid-User Cheese

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

bot.run("")