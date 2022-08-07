import discord
import asyncio
import datetime as dt
from discord.ext import commands,tasks

TOKEN = 'YOUR TOKEN HERE'

BOT_PREFIX = "$"

channel_id = YOUR CHANNEL ID NUMBER HERE

client = commands.Bot(command_prefix = BOT_PREFIX)

client.remove_command('help')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('-'))
    msg1.start()

# Message 1
@tasks.loop(hours=24)
async def msg1():
    message_channel = client.get_channel(channel_id)
    if dt.datetime.today().weekday() == 0:
        await message_channel.send("It's Monday. Beep-boop")
    if dt.datetime.today().weekday() == 1:
        await message_channel.send("It's Tuesday. Beep-boop")
    if dt.datetime.today().weekday() == 2:
        await message_channel.send("It's Wednesday. Beep-boop")
    if dt.datetime.today().weekday() == 3:
        await message_channel.send("It's Thursday. Beep-boop")
    if dt.datetime.today().weekday() == 4:
        await message_channel.send("It's Friday. Beep-boop")
    if dt.datetime.today().weekday() == 5:
        await message_channel.send("It's Saturday. Beep-boop")
    if dt.datetime.today().weekday() == 6:
        await message_channel.send("It's Sunday. Beep-boop")

@msg1.before_loop
async def before_msg1():
    for _ in range(60*60*24):  # loop the whole day
        if dt.datetime.now().hour == 7:  # 24 hour format
            print('It is time')
            return
        await asyncio.sleep(1)# wait a second before looping again. You can make it more 

client.run(TOKEN)
