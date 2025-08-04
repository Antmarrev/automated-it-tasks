import platform
import psutil
from datetime import datetime
from pathlib import Path
import socket
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def generar_reporte():
    try:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        carpeta = Path("reports")
        carpeta.mkdir(exist_ok=True)
        nombre_archivo = carpeta / f"report_{now}.txt"

        with nombre_archivo.open("w", encoding="utf-8") as f:
            f.write("🧠 INFORME DEL SISTEMA\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Equipo: {socket.gethostname()}\n")
            f.write("-" * 40 + "\n")

            f.write(f"Sistema: {platform.system()} {platform.release()}\n")
            f.write(f"Versión: {platform.version()}\n")
            f.write(f"Arquitectura: {platform.machine()}\n")
            f.write(f"Procesador: {platform.processor()}\n\n")

            f.write("🔧 CPU\n")
            f.write(f" Núcleos físicos: {psutil.cpu_count(logical=False)}\n")
            f.write(f" Núcleos lógicos: {psutil.cpu_count(logical=True)}\n")
            f.write(f" Uso actual: {psutil.cpu_percent(interval=1)}%\n\n")

            mem = psutil.virtual_memory()
            f.write("💾 Memoria\n")
            f.write(f" Total: {mem.total / (1024 ** 3):.2f} GB\n")
            f.write(f" Usada: {mem.used / (1024 ** 3):.2f} GB ({mem.percent}%)\n")
            f.write(f" Libre: {mem.available / (1024 ** 3):.2f} GB\n\n")

            disco = psutil.disk_usage("/")
            f.write("💽 Disco (/)\n")
            f.write(f" Total: {disco.total / (1024 ** 3):.2f} GB\n")
            f.write(f" Usado: {disco.used / (1024 ** 3):.2f} GB ({disco.percent}%)\n")
            f.write(f" Libre: {disco.free / (1024 ** 3):.2f} GB\n\n")

            f.write("📋 Procesos activos (Top 5 por RAM)\n")
            procesos = sorted(
                [p for p in psutil.process_iter(['pid', 'name', 'memory_info']) if p.info.get('memory_info')],
                key=lambda p: p.info['memory_info'].rss,
                reverse=True
            )
            for p in procesos[:5]:
                try:
                    mem_mb = p.info['memory_info'].rss / (1024 ** 2)
                    f.write(f" PID {p.info['pid']} - {p.info['name']} - {mem_mb:.2f} MB\n")
                except Exception:
                    continue

        print(f"✅ Informe generado: {nombre_archivo.absolute()}")

    except Exception as e:
        print(f"[ERROR] No se pudo generar el informe: {e}")

if __name__ == "__main__":
    generar_reporte()
