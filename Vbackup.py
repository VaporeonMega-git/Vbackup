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

bot.run("")