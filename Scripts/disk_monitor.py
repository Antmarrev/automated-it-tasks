import shutil
import argparse
import platform
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def get_disk_usage(path="/"):
    usage = shutil.disk_usage(path)
    total = usage.total
    used = usage.used
    percent_used = (used / total) * 100
    return total, used, percent_used

def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

def mostrar_estado(total, used, percent, threshold_warning=85, threshold_critical=95, dry_run=False):
    estado = "🟢 OK"
    if percent >= threshold_critical:
        estado = "🔴 CRÍTICO"
    elif percent >= threshold_warning:
        estado = "🟠 ADVERTENCIA"

    print(f"💽 Uso de disco:")
    print(f"   Total: {bytes_to_gb(total)} GB")
    print(f"   Usado: {bytes_to_gb(used)} GB ({percent:.2f}%)")
    print(f"   Estado: {estado}")

    if dry_run:
        print("[SIMULACIÓN] No se realiza ninguna acción.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitoreo de uso de disco")
    parser.add_argument('--path', type=str, default="/", help='Ruta del disco a monitorear (por defecto / o C:\\)')
    parser.add_argument('--dry-run', action='store_true', help='Simula el monitoreo sin acciones reales')
    args = parser.parse_args()

    # En Windows, usar C:\ si no se especifica
    if platform.system() == "Windows" and args.path == "/":
        args.path = "C:\\"

    total, used, percent = get_disk_usage(args.path)
    mostrar_estado(total, used, percent, dry_run=args.dry_run)
