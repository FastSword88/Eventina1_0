# Eventina - Discord Movie Night Bot 🎬

![Bot Status](https://img.shields.io/badge/status-active-brightgreen) ![Python](https://img.shields.io/badge/python-3.8+-blue) ![Discord.py](https://img.shields.io/badge/discord.py-2.0+-7289da)

**Eventina** is a multifunctional Discord bot designed to organize and manage movie nights with your community. In addition to scheduling features, it includes additional capabilities such as synopsis lookup, streaming platform search, and useful tools.

## ✨ Main Features

- **🎬 Movie Night Scheduling**: Schedule movies with specific dates and times
- **📖 Synopsis Lookup**: Get movie summaries using Gemini AI
- **📱 Platform Search**: Discover which streaming services have each movie
- **📊 Statistics**: Monitor the status of your scheduled movie nights
- **⏰ Automatic Reminders**: Notifications for upcoming events
- **🛠️ Additional Tools**: Useful functions for server management

## 🤖 Available Commands

### 🎬 Movie Commands
| Command | Description | Example |
|---------|-------------|---------|
| `!pelicula "<name>" "<date>" "<time>"` | Schedule a movie for group viewing | `!pelicula "Avengers" "2024-12-25" "20:00"` |
| `!listar_peliculas` | Shows all scheduled movies with their details | `!listar_peliculas` |
| `!eliminar_pelicula <ID>` | Deletes a scheduled movie using its ID | `!eliminar_pelicula 3` |
| `!limpiar_peliculas` | Performs manual cleanup of watched movies | `!limpiar_peliculas` |

### 📖 Movie Information
| Command | Description | Example |
|---------|-------------|---------|
| `!sinopsis` | Provides the synopsis of a movie | `!sinopsis Titanic` |
| `!plataformas` | Shows where a movie is available | `!plataformas Inception` |

### 📊 Management and Statistics
| Command | Description | Example |
|---------|-------------|---------|
| `!estadisticas` | Shows movie statistics | `!estadisticas` |
| `!hora` | Shows the current time in Mexico City (CDMX) | `!hora` |


## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Discord Developer account
- Discord bot token
- Gemini API Key (for synopsis features)

