aqui tengo mi codigo! perdon por la tardanza
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io

Crear el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

Comando para generar una imagen
@bot.command()
async def reciclaje(ctx):
    # Crear una imagen con fondo verde
    img = Image.new('RGB', (500, 250), color=(34, 177, 76))  # Color verde
    draw = ImageDraw.Draw(img)

    # Usar una fuente estándar
    font = ImageFont.load_default()

    # Escribir un mensaje en la imagen
    mensaje = "¡Recicla y cuida el planeta!"
    textwidth, textheight = draw.textsize(mensaje, font=font)
    position = ((img.width - textwidth) // 2, (img.height - textheight) // 2)

    # Escribir el texto en la imagen
    draw.text(position, mensaje, font=font, fill=(255, 255, 255))

    # Crear un archivo de imagen en memoria
    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)

        # Enviar la imagen al canal de Discord
        await ctx.send("Aquí tienes tu mensaje de reciclaje:", file=discord.File(fp=image_binary, filename='reciclaje.png'))

Comando de bienvenida
@bot.event
async def on_ready():
    print(f'Bot {bot.user} ha iniciado sesión correctamente en Discord!')

Enviar un mensaje de bienvenida al canal general
    general_channel = discord.utils.get(bot.get_all_channels(), name='general')
    if general_channel:
        await general_channel.send("¡Bienvenidos al servidor! Juntos podemos hacer un impacto positivo en el planeta. 🌍💚")
Emilioo — hoy a las 16:54
ya tengo mi pedazo de codigo 🙂
import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

Declaramos el temporizador como una tarea de fondo
@tasks.loop(hours=24)  # Se ejecutará cada 24 horas
async def daily_timer(channel):
    if channel:
        await channel.send("Este es tu recordatorio diario de reciclar!!")

@daily_timer.before_loop
async def before_daily_timer():
    print("Esperando que el bot esté listo para iniciar el temporizador...")
    await bot.wait_until_ready()  # Asegura que el bot esté completamente conectado antes de iniciar el temporizador

Comando para iniciar el temporizador
@bot.command()
async def timer(ctx):
    if not daily_timer.is_running():  # Verifica si el temporizador ya está corriendo
        await ctx.send("Temporizador de 24 horas iniciado.")
        daily_timer.start(ctx.channel)  # Inicia el temporizador en el canal actual
    else:
        await ctx.send("El temporizador ya está en ejecución.")

Comando para detener el temporizador
@bot.command()
async def stoptimer(ctx):
    if daily_timer.is_running():  # Verifica si el temporizador está corriendo
        daily_timer.cancel()  # Detiene el temporizador
        await ctx.send("El temporizador se detuvo.")
    else:
        await ctx.send("El temporizador no está en ejecución.")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Ocurrió un error: {error}')
    print(f'Error en el comando: {error}')


bot.run("token")
