import discord
import asyncio
from discord.ext import commands
import ffmpeg
import random
from funct import *


client = discord.Client()


@client.event 
async def on_ready():
    print("Rodando!!")
    user = client.get_user(client.user.id)
    
@client.event 
async def on_message(message):
    try:
        channelV = message.author.voice.channel
    except:
         pass   
    channel = message.channel
    

    if message.content.upper() == "BOT":
        try:
           print(channelV)
           vc = await channelV.connect()
           pass
        except:
           print(f"bot ja está conectado no canal {channel}")
           pass
    
    if pal_check(message.content.upper()):
        with open("./resp_pal.txt","r") as respostas:
           
           resp =random.randint(0,int(respostas.readline()))
           for i in range(1,resp):
               respostas.readline()
           await channel.send("@"+message.author.name+" " +respostas.readline())
        await message.delete()
        
        
        


client.run("NzcxNDc3MDg3NTYyMjM1OTc0.X5ssBw.MqlVxrdhd7MgbkyhcYFw1f-AFhM")

