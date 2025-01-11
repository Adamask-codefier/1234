import discord
from discord.ext import commands
from Dado import lanzar_dado

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='?', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def dado(ctx):
    resultado = lanzar_dado()  # Llamamos la función para lanzar el dado
    await ctx.send(f"🎲 El resultado del dado fue: {resultado}")    

bot.run(".")
