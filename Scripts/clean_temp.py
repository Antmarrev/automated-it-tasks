import os
import shutil
import platform
import argparse
from pathlib import Path

import sys
sys.stdout.reconfigure(encoding='utf-8')


def get_temp_paths():
    temp_path = os.environ.get("TEMP")
    if not temp_path:
        raise EnvironmentError("No se pudo obtener la ruta temporal (TEMP) en Windows.")
    return [Path(temp_path)]

def clean_temp_folder(path: Path, dry_run=False):
    files_deleted = 0
    space_freed = 0

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            try:
                file_path = Path(root) / name
                size = file_path.stat().st_size
                if dry_run:
                    print(f"[SIMULACIÓN] Se eliminaría: {file_path} ({human_readable_size(size)})")
                else:
                    file_path.unlink()
                files_deleted += 1
                space_freed += size
            except Exception as e:
                print(f"[!] No se pudo eliminar {file_path}: {e}")

        for name in dirs:
            try:
                dir_path = Path(root) / name
                if dry_run:
                    print(f"[SIMULACIÓN] Se eliminaría carpeta: {dir_path}")
                else:
                    shutil.rmtree(dir_path, ignore_errors=True)
            except Exception as e:
                print(f"[!] No se pudo eliminar carpeta {dir_path}: {e}")

    return files_deleted, space_freed

def human_readable_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Limpia archivos temporales del sistema")
    parser.add_argument('--dry-run', action='store_true', help='Simula la limpieza sin borrar nada')
    args = parser.parse_args()

    print("🧹 Limpieza de carpetas temporales...")
    if args.dry_run:
        print("🔍 MODO SIMULACIÓN ACTIVADO (no se eliminará nada)\n")

    total_files = 0
    total_space = 0

    for temp_path in get_temp_paths():
        print(f"📁 Revisando: {temp_path}")
        files, space = clean_temp_folder(temp_path, dry_run=args.dry_run)
        print(f"✅ {files} archivos detectados – {human_readable_size(space)}\n")
        total_files += files
        total_space += space

    print("🏁 Limpieza finalizada" if not args.dry_run else "🏁 Simulación completada")
    print(f"🧾 Total: {total_files} archivos, {human_readable_size(total_space)}")
