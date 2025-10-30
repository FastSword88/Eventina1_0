from datetime import datetime, timedelta
import pytz

# Configurar zona horaria de CDMX
ZONA_HORARIA = pytz.timezone('America/Mexico_City')

def ahora_cdmx():
    """Obtener la fecha y hora actual en CDMX"""
    return datetime.now(ZONA_HORARIA)

def crear_fecha_cdmx(fecha_str, hora_str):
    """Crear un objeto datetime con zona horaria de CDMX"""
    fecha_hora_str = f"{fecha_str} {hora_str}"
    fecha_hora_naive = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
    return ZONA_HORARIA.localize(fecha_hora_naive)

def formatear_fecha(fecha_hora):
    """Formatear fecha para mostrar"""
    return fecha_hora.strftime("%d/%m/%Y a las %H:%M")