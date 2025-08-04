import subprocess
import argparse
import sys

scripts = [
    ("🧹 Limpieza de temporales", "scripts/clean_temp.py"),
    ("📦 Instalador de apps", "scripts/silent_installer.py"),
    ("💾 Backup automático", "scripts/backup_scheduler.py"),
    ("💽 Monitor de disco", "scripts/disk_monitor.py"),
    ("🧠 Reporte del sistema", "scripts/report_generator.py")
]

def ejecutar(script_path, dry_run):
    comando = [sys.executable, script_path]
    if dry_run and "report_generator" not in script_path:  # no tiene --dry-run
        comando.append("--dry-run")
    try:
        print(f"\n➡️ Ejecutando: {script_path}")
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando {script_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecuta todos los scripts de automated-it-tasks")
    parser.add_argument('--dry-run', action='store_true', help='Simula las tareas sin cambios reales')
    args = parser.parse_args()

    for titulo, ruta in scripts:
        print(f"\n=== {titulo} ===")
        ejecutar(ruta, dry_run=args.dry_run)
