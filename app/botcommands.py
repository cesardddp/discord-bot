
import discord
from discord.ext import commands
import funct
bot = commands.Bot(command_prefix='$')

@bot.command()
async def repetir(ctx, *args):
 try:
     for i in range(0,int(args[0])):
       await ctx.send(" ".join(args))
       i+=1
    
 except:
     await ctx.send(" ".join(args))
     pass
  
@bot.command()
async def somar(ctx, *args):
  soma = 0
  string =""
  for i in args:
      string = string + i +" + "
      soma = soma + int(i)
  string = string + "= "+str(soma)
  await ctx.send(string)
    
@bot.command()
async def clear(ctx, *args):
  print("entrei")
  def check_palavras(m):
        
        #import ipdb; ipdb.set_trace()
        return funct.pal_check(m.content.upper())
        
  deleted = await ctx.message.channel.purge(limit=100, check=check_palavras)
  #await channel.send('Deleted {} message(s)'.format(len(deleted)))



bot.run("NzcxNDc3MDg3NTYyMjM1OTc0.X5ssBw.MqlVxrdhd7MgbkyhcYFw1f-AFhM")