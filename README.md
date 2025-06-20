# CurseForge Mod Downloader

Este script descarga automáticamente todos los mods listados en un archivo `manifest.json` (formato CurseForge modpack).

## Requisitos
- Python 3.8+
- Una API Key gratuita de CurseForge: https://console.curseforge.com/?#/api-keys

## Instalación
1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Coloca tu archivo `manifest.json` en la ruta indicada en el script (por defecto: `C:\Users\marti\Desktop\test1.21.1\manifest.json`).
3. Establece tu API Key de CurseForge:
   - Puedes editar el script y poner tu API Key en la variable `CURSEFORGE_API_KEY`,
   - O establecer la variable de entorno `CURSEFORGE_API_KEY`.

## Uso

```sh
python download_mods.py
```

Los mods se descargarán en la carpeta `mods/`.

---

Si tienes dudas o necesitas adaptar la ruta del manifest, avísame.
