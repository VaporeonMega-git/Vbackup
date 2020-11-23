import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    await ctx.send("This command is still in development")

bot.run("")