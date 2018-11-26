import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='w!')
bot.remove_command('help')
ownerID = "274298631517896704"
Error = 0xFF0000


# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
            
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing " + mesg)
    
@bot.command(pass_context=True)
async def watching(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=3))
    
@bot.command(pass_context=True)
async def listening(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=2))
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
  if ctx.message.author.id in ownerID:
  
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=ctx.message.author.color)
    embed.add_field(name='Name', value='{}'.format(user.name))
    embed.add_field(name='ID', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
    embed.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
    embed.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
    embed.add_field(name='Discriminator', value='{}'.format(user.discriminator), inline=True)
    embed.add_field(name='Playing', value='{}'.format(user.game))
    embed.set_footer(text="{}'s Info".format(user.name), icon_url='{}'.format(user.avatar_url))
    embed.set_thumbnail(url=user.avatar_url)
  
    await bot.say(embed=embed)
        
@bot.command(pass_context=True)
async def prune(ctx, number, *args):
  if ctx.message.author.id in ownerID:
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
    
@bot.command(passcontext=True)
async def rpinfo()

embed = discord.Embed(name='List of characters', discription=None, color=0x0053d8)
embed.set_author(ctx.message.author.name)
embed.add_field(name='Kenki', value=None, inline=False)
embed.add_field(name='Xenzai', value=None, inline=False)
embed.add_field(name='Chara', value=None, inline=False)
embed.add_field(name='Nine', value=None, inline=False)
embed.add_field(name='Yuri', value=None, inline=False)
embed.add_field(name='Gio', value=None, inline=False)


await bot.say(embed=embed)
        
    

  




bot.run(os.environ.get('Token'))
