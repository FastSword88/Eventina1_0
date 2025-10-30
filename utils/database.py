import os
import json

PELICULAS_FILE = "peliculas.json"

def cargar_peliculas():
    """Cargar películas desde el archivo JSON"""
    if os.path.exists(PELICULAS_FILE):
        with open(PELICULAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_peliculas(peliculas):
    """Guardar películas en el archivo JSON"""
    with open(PELICULAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(peliculas, f, ensure_ascii=False, indent=2)

def obtener_proximo_id():
    """Obtener el próximo ID disponible"""
    peliculas = cargar_peliculas()
    return max([p["id"] for p in peliculas], default=0) + 1