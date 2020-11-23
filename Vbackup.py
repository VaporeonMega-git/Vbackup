import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    await member.kick()

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    await member.ban()

@bot.command(pass_context=True,aliases=["randomnum","randnum"])
async def randomnumber(ctx, num1: int, num2: int):
    rand = random.randint(num1,num2)
    await ctx.send("Your random number is " + str(rand))

bot.run("")