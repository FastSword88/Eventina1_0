import discord
from discord.ext import commands, tasks
from datetime import timedelta
from utils.database import cargar_peliculas, guardar_peliculas, obtener_proximo_id
from utils.time_utils import ahora_cdmx, crear_fecha_cdmx, formatear_fecha

class Peliculas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.verificar_recordatorios.start()

    @tasks.loop(seconds=60)
    async def verificar_recordatorios(self):
        """Verificar si hay películas que recordar usando hora de CDMX"""
        ahora = ahora_cdmx()
        peliculas = cargar_peliculas()
        peliculas_actualizadas = []
        
        for pelicula_data in peliculas:
            if pelicula_data["notificado"]:
                peliculas_actualizadas.append(pelicula_data)
                continue
            
            # Recuperar la fecha/hora con zona horaria
            if "fecha_hora_tz" in pelicula_data:
                from datetime import datetime
                fecha_hora = datetime.fromisoformat(pelicula_data["fecha_hora_tz"])
            else:
                # Para compatibilidad con datos antiguos
                fecha_hora = crear_fecha_cdmx(pelicula_data["fecha_hora"].split()[0], pelicula_data["fecha_hora"].split()[1])
            
            tiempo_restante = fecha_hora - ahora
            
            # Si faltan 2 horas o menos para la película
            if timedelta(hours=0) <= tiempo_restante <= timedelta(hours=2):
                try:
                    canal = self.bot.get_channel(pelicula_data["canal_id"])
                    if canal:
                        mensaje = f"@everyone 🎬 **Recordatorio** 🎬\nNo olviden que tienen que ver **{pelicula_data['nombre']}** a las **{fecha_hora.strftime('%H:%M')}** (hora CDMX)!"
                        await canal.send(mensaje)
                        
                        # Marcar como notificado
                        pelicula_data["notificado"] = True
                        print(f"✅ Recordatorio enviado para: {pelicula_data['nombre']} a las {fecha_hora.strftime('%H:%M')} CDMX")
                        
                except Exception as e:
                    print(f"❌ Error enviando recordatorio: {e}")
            
            peliculas_actualizadas.append(pelicula_data)
        
        # Guardar cambios
        guardar_peliculas(peliculas_actualizadas)

    @verificar_recordatorios.before_loop
    async def before_verificar_recordatorios(self):
        """Esperar a que el bot esté listo antes de iniciar las verificaciones"""
        await self.bot.wait_until_ready()

    @commands.command()
    async def pelicula(self, ctx, nombre: str, fecha: str, hora: str):
        """Guardar una nueva película con fecha y hora"""
        
        # Parsear fecha y hora
        try:
            fecha_hora = crear_fecha_cdmx(fecha, hora)
            
            # Verificar que la fecha no sea en el pasado (usando hora de CDMX)
            if fecha_hora < ahora_cdmx():
                await ctx.send("❌ No puedes programar películas en el pasado!")
                return
            
        except ValueError:
            await ctx.send("❌ Formato de fecha/hora incorrecto. Usa: `!pelicula \"Nombre\" \"YYYY-MM-DD\" \"HH:MM\"`")
            return
        
        # Crear objeto de película
        nueva_pelicula = {
            "id": obtener_proximo_id(),
            "nombre": nombre,
            "fecha_hora": f"{fecha} {hora}",
            "fecha_hora_tz": fecha_hora.isoformat(),
            "timestamp": fecha_hora.timestamp(),
            "canal_id": ctx.channel.id,
            "guild_id": ctx.guild.id,
            "notificado": False
        }
        
        # Guardar en la lista
        peliculas = cargar_peliculas()
        peliculas.append(nueva_pelicula)
        guardar_peliculas(peliculas)
        
        fecha_formateada = formatear_fecha(fecha_hora)
        await ctx.send(f"✅ Película **{nombre}** programada para el {fecha_formateada} (hora CDMX)")

    @commands.command()
    async def listar_peliculas(self, ctx):
        """Listar todas las películas programadas"""
        peliculas = cargar_peliculas()
        
        if not peliculas:
            await ctx.send("📝 No hay películas programadas.")
            return
        
        embed = discord.Embed(title="🎬 Películas Programadas", color=0x00ff00)
        
        for pelicula_data in peliculas:
            if "fecha_hora_tz" in pelicula_data:
                from datetime import datetime
                fecha_hora = datetime.fromisoformat(pelicula_data["fecha_hora_tz"])
            else:
                fecha_hora = crear_fecha_cdmx(pelicula_data["fecha_hora"].split()[0], pelicula_data["fecha_hora"].split()[1])
                
            estado = "✅ Notificado" if pelicula_data["notificado"] else "⏰ Pendiente"
            
            embed.add_field(
                name=f"{pelicula_data['nombre']} (ID: {pelicula_data['id']})",
                value=f"📅 **Fecha:** {fecha_hora.strftime('%d/%m/%Y')}\n"
                      f"⏰ **Hora:** {fecha_hora.strftime('%H:%M')} CDMX\n"
                      f"🔔 **Estado:** {estado}",
                inline=False
            )
        
        await ctx.send(embed=embed)

    @commands.command()
    async def eliminar_pelicula(self, ctx, id: int):
        """Eliminar una película programada"""
        peliculas = cargar_peliculas()
        peliculas_actualizadas = [p for p in peliculas if p["id"] != id]
        
        if len(peliculas_actualizadas) == len(peliculas):
            await ctx.send("❌ No se encontró una película con ese ID.")
            return
        
        guardar_peliculas(peliculas_actualizadas)
        await ctx.send("✅ Película eliminada correctamente.")

async def setup(bot):
    await bot.add_cog(Peliculas(bot))