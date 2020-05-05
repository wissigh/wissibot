import asyncio

import ctx as ctx
import discord
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot, guild_only


bot = commands.Bot(command_prefix="$", description="")

@bot.event
async def on_ready():
    print('The Wissi Bot is ready')
    bot.loop.create_task(status_task())

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('$help for Commands!'), status=discord.Status.online)
        await asyncio.sleep(5)




def is_not_pinned(mess):
    return not mess.pinned






@bot.command()
async def wissiyt(ctx):
  """
  YouTube Link for the Channel Wissi
  """
  await ctx.send('https://www.youtube.com/channel/UCewbBRQHd9HMii6eXUUVV5A')

@bot.command()
async def ridayt(ctx):
  """
  YouTube Link for the Channel Wissi
  """
  await ctx.send('https://www.youtube.com/channel/UCrEQKnUrRh-54zgwNa0UN8w')

@bot.command(aliases=["wissi?"])
async def _wissi(ctx):
  """
  Checks the Status of Wissi
  """
  await ctx.send("Wissi is currently unavailable.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
  """
  cleans a given amount of messages in a channel
  """
  await ctx.channel.purge(limit=limit)
  await ctx.send(f'Wissi cleared {limit} off the runway successfully!', delete_after=5)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, args):
  """
  Kicks a memeber out of the server
  """
  await ctx.guild.kick(member)
  await ctx.send(f"{member} has been kicked from the server by {ctx.author.mention}! reason: {args}")


@bot.command()
@commands.has_any_role("CEO","Wissi Bot")
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "You broke the rules!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")


client = commands.Bot(command_prefix='$')

@bot.command()
@commands.has_any_role("CEO","Moderator")
async def _yt(ctx):
  await ctx.send('Hey! How about to check out my YouTube Channel! \n\rhttps://www.youtube.com/channel/UCewbBRQHd9HMii6eXUUVV5A')
  await asyncio.sleep(34560)


  client.loop.create_task(_yt(ctx))





bot.run('NzAxOTM0NzQxOTEzMzM3OTQ3.Xp9H6w.VQXSX4HrZRIL6w8Kz9R6qq4LfSc')