import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()

# Configurar los intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🤖 Bot conectado como {bot.user}')
    print('✅ Todos los módulos cargados correctamente')

async def load_cogs():
    """Cargar todos los módulos del bot"""
    await bot.load_extension('cogs.peliculas')
    await bot.load_extension('cogs.utilidades')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())