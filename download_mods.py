import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
CURSEFORGE_API_KEY = os.environ.get('CURSEFORGE_API_KEY')

MANIFEST_PATH = r'C:\workspace\download_mods\manifest.json' # ruta del archivo manifest.json
MODS_FOLDER = 'mods' # carpeta donde se guardarán los mods
API_BASE = 'https://api.curseforge.com/v1'

headers = {
    'Accept': 'application/json',
    'x-api-key': CURSEFORGE_API_KEY
}

def ensure_mods_folder():
    if not os.path.exists(MODS_FOLDER):
        os.makedirs(MODS_FOLDER)

def get_mod_download_url(project_id, file_id):
    url = f"{API_BASE}/mods/{project_id}/files/{file_id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"No se pudo obtener info para el mod {project_id}/{file_id}")
        return None
    data = resp.json()
    return data['data'].get('downloadUrl')

def download_mod(url, filename):
    print(f"Descargando {filename}...")
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(os.path.join(MODS_FOLDER, filename), 'wb') as f:
            f.write(resp.content)
        print(f"Guardado: {filename}")
    else:
        print(f"Error al descargar {filename}")

def main():
    if CURSEFORGE_API_KEY == None:
        print("Por favor, pon tu API Key de CurseForge en la variable CURSEFORGE_API_KEY o como variable de entorno.")
        return
    ensure_mods_folder()
    with open(MANIFEST_PATH, encoding='utf-8') as f:
        manifest = json.load(f)
    for entry in manifest.get('files', []):
        project_id = entry['projectID']
        file_id = entry['fileID']
        url = get_mod_download_url(project_id, file_id)
        if url:
            filename = url.split('/')[-1]
            download_mod(url, filename)
        else:
            print(f"No se encontró URL para {project_id}/{file_id}")

if __name__ == '__main__':
    main()
