import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description= "Bot ParcourSup")

@bot.event
async def on_ready() :
    print(' Je suis en ligne ! Enchanté de vous rencontrer !')
    print('-------')

@bot.command()
async def Bonjour(ctx) :
    await ctx.send("Enchanté ! Je suis le ParcourSup Bot ! J'ai été crée par Jad SAMAIN afin de montrer ses divers compétences en programmation Python. N'hésitez surtout pas à le contacter si vous avez des questions :) !")

@bot.command()
async def Date(ctx) :
    await ctx.send("La date finale à laquelle les élèves peuvent envoyer est le 29 mars, il ne faut pas oublier d'envoyer ses voeux !!! ")

@bot.command()
async def Ecoles(ctx):
    await ctx.send("Tu veux proposer des écoles qui pourront te fournir une formation dans l'informatique, afin de devenir Data Analyst, c'est ça?")

@bot.command()
async def Heure(ctx):
    await ctx.send("Il est actuellement 21h02 !")

@bot.command()
async def Merci(ctx):
    await ctx.send("Pas de soucis !")

@bot.command()
async def Etudes(ctx):
    await ctx.send("Je pense que tu devrais faire des études d'informatique, puis un master et enfin une formation ! Comme ça tu seras un bon Data Analyst !!")

bot.run("OTM5ODI1NjM5MTQ4NjMwMDM2.Yf-e1Q.f9FLM0IqsReC0iakC6YZMY7gZ-o")