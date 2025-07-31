import subprocess
import platform
import argparse
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def is_windows():
    return platform.system() == "Windows"

def leer_lista_apps(archivo):
    path = Path(archivo)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {archivo}")
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def app_instalada(app_id):
    try:
        result = subprocess.run(["winget", "list", "--id", app_id], capture_output=True, text=True)
        return app_id.lower() in result.stdout.lower()
    except Exception:
        return False

def instalar_app(app_id, dry_run=False):
    if app_instalada(app_id):
        print(f"[OMITIDA] Ya instalada: {app_id}")
        return

    if dry_run:
        print(f"[SIMULACION] Se instalaria: {app_id}")
    else:
        print(f"📦 Instalando {app_id}...")
        try:
            subprocess.run(["winget", "install", "--id", app_id, "-e", "--silent"], check=True)
            print(f"✅ {app_id} instalado correctamente\n")
        except subprocess.CalledProcessError as e:
            if e.returncode == 2147943623:
                print(f"⚠️ Instalación cancelada por el usuario: {app_id}\n")
            else:
                print(f"❌ Error al instalar {app_id}: {e}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instalador silencioso de apps usando winget")
    parser.add_argument('--dry-run', action='store_true', help='Simula la instalación sin ejecutar comandos')
    args = parser.parse_args()

    if not is_windows():
        print("Este script solo funciona en Windows con winget instalado.")
        exit(1)

    try:
        lista_apps = leer_lista_apps("apps.txt")
        for app in lista_apps:
            instalar_app(app, dry_run=args.dry_run)
    except Exception as e:
        print(f"[ERROR] {e}")
