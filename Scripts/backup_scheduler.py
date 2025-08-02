import os
import shutil
import json
import time
from datetime import datetime
from pathlib import Path
import argparse
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def cargar_configuracion(ruta="C:\\Users\\anton\\OneDrive\\Desktop\\automated-it-tasks\\Scripts\\backup_config.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        config = json.load(f)
    return Path(config["origen"]), Path(config["destino"])

def crear_backup(origen, destino, dry_run=False):
    if not origen.exists():
        print(f"[ERROR] La ruta de origen no existe: {origen}")
        return

    timestamp = datetime.now().strftime("backup_%Y-%m-%d_%H-%M-%S")
    destino_final = destino / timestamp

    if dry_run:
        print(f"[SIMULACION] Se copiaría: {origen} -> {destino_final}")
        return

    try:
        shutil.copytree(origen, destino_final)
        print(f"✅ Backup creado: {destino_final}")
        registrar_log(f"Backup creado: {destino_final}")
    except Exception as e:
        print(f"[ERROR] No se pudo crear el backup: {e}")
        registrar_log(f"ERROR al crear backup: {e}")

def registrar_log(mensaje):
    log_file = Path("backup_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {mensaje}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup de carpetas con registro")
    parser.add_argument('--dry-run', action='store_true', help='Simula la copia sin ejecutarla')
    args = parser.parse_args()

    origen, destino = cargar_configuracion()
    crear_backup(origen, destino, dry_run=args.dry_run)
