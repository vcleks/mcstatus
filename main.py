import discord
import json
from discord.ext import commands
from mcstatus import MinecraftServer

#token config thing
with open('config.json') as f:
    config = json.loads(f.read())
    TOKEN = config['token']
    PREFIX = config['prefix']


#stuff
bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True)

# vanilla
vanilla = MinecraftServer("SERVERIP", PORT)
vanillastatus = vanilla.status()
vanillaquery = vanilla.query()

# Modded
modded = MinecraftServer("SERVERIP", PORT)
moddedstatus = modded.status()
moddedquery = modded.query()


# game = discord.Game(name="with {0} players".format(status.players.online))


@bot.event
async def on_ready():
    print('Connected to discord using {0.user}'.format(bot))





@bot.command(name='players', description='Player list')
async def players(ctx):
    embed = discord.Embed(title="MC Status", color=0x1fab96)
    embed.add_field(name="Players Online ", value="`{0}`".format(", ".join(vanillaquery.players.names)), inline=False)
    embed.add_field(name="Players Online ", value="`{0}`".format(", ".join(moddedquery.players.names)), inline=False)
    embed.set_footer(text="Requested by {0}".format(ctx.message.author))
    await ctx.send(embed=embed)

@bot.command(name='info', description='Info on the server')
async def info(ctx):
    embed = discord.Embed(title="Mc Status", color=0x1fab96)
    embed.add_field(name="Vanilla Server IP", value="`SERVERIP`", inline=False)
    embed.add_field(name="Modded Server IP", value="`SERVERIP`", inline=False)
    embed.set_footer(text="Requested by {0}".format(ctx.message.author))
    await ctx.send(embed=embed)




bot.run(TOKEN)
