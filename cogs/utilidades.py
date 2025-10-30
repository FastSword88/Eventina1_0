import discord
from discord.ext import commands
from utils.time_utils import ahora_cdmx

class Utilidades(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='suma')
    async def sumar(self, ctx, num1, num2):
        """Realizar suma de dos números"""
        try:
            response = int(num1) + int(num2)
            await ctx.send(f"🔢 Resultado: {response}")
        except ValueError:
            await ctx.send("❌ Por favor ingresa números válidos")

    @commands.command()
    async def hora(self, ctx):
        """Muestra la hora actual en CDMX"""
        ahora = ahora_cdmx()
        await ctx.send(f"🕐 **Hora actual en CDMX:** {ahora.strftime('%d/%m/%Y %H:%M:%S')}")

    @commands.command()
    async def comandos(self, ctx):
        """Muestra todos los comandos disponibles del bot"""
        
        embed = discord.Embed(
            title="🤖 Comandos Disponibles",
            description="Aquí tienes la lista de todos los comandos que puedes usar:",
            color=0x0099ff
        )
        
        embed.add_field(
            name="🔢 `!suma <número1> <número2>`",
            value="Realiza la suma de dos números.\n**Ejemplo:** `!suma 5 3`",
            inline=False
        )
        
        embed.add_field(
            name="🎬 `!pelicula \"<nombre>\" \"<fecha>\" \"<hora>\"`",
            value="Programa una película para ver en grupo.\n**Formato fecha:** YYYY-MM-DD\n**Formato hora:** HH:MM\n**Ejemplo:** `!pelicula \"Avengers\" \"2024-12-25\" \"20:00\"`",
            inline=False
        )
        
        embed.add_field(
            name="📋 `!listar_peliculas`",
            value="Muestra todas las películas programadas con sus detalles.",
            inline=False
        )
        
        embed.add_field(
            name="🗑️ `!eliminar_pelicula <ID>`",
            value="Elimina una película programada usando su ID.\n**Nota:** Usa `!listar_peliculas` para ver los IDs.",
            inline=False
        )
        
        embed.add_field(
            name="🕐 `!hora`",
            value="Muestra la hora actual en CDMX.",
            inline=False
        )
        
        embed.add_field(
            name="ℹ️ `!comandos`",
            value="Muestra esta lista de comandos disponibles.",
            inline=False
        )
        
        embed.set_footer(text="¡Diviértete usando el bot! 🎉")
        
        await ctx.send(embed=embed)

    @commands.command()
    async def ayuda(self, ctx):
        """Comando alternativo de ayuda"""
        await ctx.send("📝 Usa `!comandos` para ver la lista completa de comandos disponibles.")

async def setup(bot):
    await bot.add_cog(Utilidades(bot))