import time, random, math

import discord
from discord.ext import commands

import asyncio

import shizzle
from utils import getTime
import woordenlijst
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
    await channel.send('Im back nibbas', delete_after=5)



@bot.command()
async def tits(ctx): #i dont fucking know to 
    await ctx.send('BIG FAT TITTIES AND VEGENE', tts=True, delete_after=0.1)



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
        ctx.send('You dont have Authorization, please contact an Administator')


        
@bot.command()
async def shutdown(ctx): #shutsdown bot
    await ctx.message.delete()
    print(getTime(), ctx.author, "used ;shutdown")
    if ctx.author.id == shizzle.fuhrer_id:
        print('======================')
        print('Bot is shutting down...')
        print('======================')
        await ctx.send("Bot shutting down...", delete_after=3)
        await asyncio.sleep(3)
        await bot.logout()
    else:
        ctx.send('You dont have Authorization, please contact an Administator')



@bot.command()
async def list(ctx, option, *, message): #Add or Remove a word to the list
    if ctx.author.id != shizzle.fuhrer_id: #Checks if its me
        print(getTime(), ctx.author, 'Tried to use addword')
        await ctx.channel.send('You dont have Authorization, please contact an Administator')
    elif option == 'add': #Adds a word
        woordenlijst.lijst.append(message)
        print(getTime(), message, 'Added to the list')
    elif option == 'remove': #Removes a word
        print(getTime(), 'Removed', message, 'From the list')
        woordenlijst.lijst.remove(message)
    else: #If all failed tell me 
        print(getTime(), 'Tried to use ;list but something went wrong')
        await ctx.channel.send('Something went wrong')



@bot.event
async def on_message(message): #Trigger all of this if there is sent a message
    if message.author.id == bot.user.id: #Check if the message came from the bot itself
        return
    elif "tinko" in message.content.lower() or "sanne" in message.content.lower(): #Everytime someone says "tinko" the bot will say a random word from the list
        await message.channel.send(content=("Tinko is een " + random.choice(woordenlijst.lijst)))
        print(getTime(), message.author, "said 'tinko' I responded :)")
    await bot.process_commands(message) #Overide on_message so the commands still trigger



'''
@bot.event
async def on_message_delete(message): #kijkt wat voor berichten mensen deleten [moet nog adden dat hij het niet bij het delete command doet]
    if message.author.id == bot.user.id:
        return
    else:
        print('==============================')
        print(message.author, 'Deleted:')
        print(getTime(), message.content)
        print('==============================')
'''



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
    if hours == 1:
        msg+= " {} Hour,".format(hours)
    elif hours != 0:
        msg+= " {} Hours,".format(hours)
    
    if minutes == 1:
        msg +=  " {} Minute,".format(minutes)
    elif minutes != 0:
        msg +=  " {} Minutes,".format(minutes)
    
    msg += " {} Seconds".format(int(seconds))

    await ctx.send(msg)

bot.run(shizzle.token)
