import time, random, math

import discord
from discord.ext import commands

import asyncio

import shizzle
from utils import getTime

# py "C:\PYTHON\Discord Makrek Bot\main.py"
bot = commands.Bot(command_prefix=';')
t1 = time.clock()


@bot.event
async def on_ready():
    print('--------------------------------------------------')
    print('Logged in as:', bot.user.name)
    print('ID: ', bot.user.id)
    print('Probably working as intented, oh no never mind...')
    print('Bot started at', getTime())
    print('--------------------------------------------------')
    await bot.change_presence(activity=discord.Activity(name='Met jou nichtje', type=discord.ActivityType.streaming))   
    channel = bot.get_channel(shizzle.bot_channel_id)
    await channel.send('Im back ni🅱️🅱️as', delete_after=5)


@bot.command()
async def delete(ctx, number=20): #deletes NUMBER amount of messages
    await ctx.message.delete()
    if ctx.author.id == shizzle.fuhrer_id:
        await ctx.send('Clearing ' + str(number) + ' messages...')
        await asyncio.sleep(1.25)
        await ctx.channel.purge(limit=int(number+2), bulk=True)
        print(getTime(), 'Marek just used the delete command.')
    else:
        await ctx.send('Boi. You are not allowed to do this shiet, fricking get out of here smiecht!!', delete_after=10)
        

@bot.command()
async def sourcecode(ctx): #sends the sourcecode
    await ctx.message.delete()
    print(getTime(), ctx.author, "used ;sourcecode")
    if ctx.author.id == shizzle.fuhrer_id:
        await ctx.send(file=discord.File(r"C:\PYTHON\Discord Makrek Bot\main.py"), delete_after=60)
    else:
        ctx.send('You dont have Authorization, pls contact Marek')

@bot.event
async def on_message(message): #check if message is from the bot itself
    if message.author.id == bot.user.id:
        return
#everytime someone says "tinko" the bot will say something
    elif "tinko" in message.content.lower():
        await message.channel.send(content=("Tinko is een " + random.choice(shizzle.nl_scheldwoord_list)))
        print(getTime(), "Someone said 'tinko' I responded :)")
#Overide on_message so it takes commands
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author.id == bot.user.id:
        return
    else:
        print(getTime(), message.content)
    
@bot.command()
async def uptime(ctx): #Shows how long the bot is online
    print(getTime(), ctx.author, "used ;uptime")
    global t1
    t2 = time.clock()
    seconds = t2-t1
    hours = math.floor(seconds/60/60)
    seconds -= hours * 60 * 60
    minutes = math.floor(seconds/60)
    seconds -= minutes * 60

    msg = 'The Bot is running'
    if hours != 0:
        msg+= " {} Hours,".format(hours)
    if minutes != 0:
        msg +=  " {} Minutes,".format(minutes)
    msg += " {} Seconds".format(int(seconds))

    await ctx.send(msg)

bot.run(shizzle.token)
