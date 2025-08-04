# ⚙️ automated-it-tasks

![Windows Only](https://img.shields.io/badge/Windows-Only-blue?logo=windows&style=for-the-badge)

🖥️ **Proyecto exclusivo para Windows 10/11**

Este repositorio contiene un conjunto de **scripts reales de automatización IT para entornos Windows**, desarrollados como toolkit personal para tareas comunes de mantenimiento, configuración y diagnóstico del sistema.

Incluye herramientas para:

- Limpiar archivos temporales
- Instalar apps silenciosamente con `winget`
- Programar backups automáticos
- Monitorear el uso de disco
- Generar reportes técnicos del sistema
- Orquestar todo con un lanzador único (`run_all.py`)

Diseñado para ser usado tras formateos, en equipos nuevos o como entorno de soporte técnico personal.

> ⚠️ Este proyecto ha sido desarrollado y probado exclusivamente para sistemas **Windows 10/11**.  
> No es compatible con Linux ni macOS.

---

## 🧰 Scripts incluidos

| Script                  | Descripción                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `clean_temp.py`        | Elimina archivos temporales del sistema y calcula espacio liberado         |
| `silent_installer.py`  | Instala aplicaciones desde `apps.txt` usando `winget`, con soporte `--dry-run` |
| `backup_scheduler.py`  | Copia una carpeta origen a un destino con timestamp y guarda un log         |
| `disk_monitor.py`      | Muestra el uso de disco actual con semáforo de estado (🟢 / 🟠 / 🔴)        |
| `report_generator.py`  | Genera un informe completo del sistema en texto (hardware, memoria, disco...) |

---

## 📄 Documentación por script

- 🧹 [Limpieza de temporales (`clean_temp.py`)](https://github.com/Antmarrev/automated-it-tasks/wiki/clean_temp)
- 📦 [Instalador silencioso (`silent_installer.py`)](https://github.com/Antmarrev/automated-it-tasks/wiki/silent_installer)
- 💾 [Backup automático (`backup_scheduler.py`)](https://github.com/Antmarrev/automated-it-tasks/wiki/backup_scheduler)
- 💽 [Monitor de disco (`disk_monitor.py`)](https://github.com/Antmarrev/automated-it-tasks/wiki/disk_monitor)
- 🧠 [Informe del sistema (`report_generator.py`)](https://github.com/Antmarrev/automated-it-tasks/wiki/report_generator)

---

## 🚀 Lanzador automático

Puedes ejecutar todos los scripts en orden con:

```bash
python run_all.py
```
O simular todo sin hacer cambios reales:
```bash
python run_all.py --dry-run
```
## 📁 Archivos auxiliares
`apps.txt` → lista de apps a instalar

`backup_config.json` – archivo de configuración para el script de backup.

```json
{
  "origen": "C:\\Ruta\\Al\\Directorio_Origen",
  "destino": "C:\\Ruta\\Al\\Directorio_Backup"
}
```

`backup_log.txt` → historial de copias realizadas

`/reports/` → informes del sistema generados automáticamente

## 📘 Documentación
Consulta la Wiki del proyecto para ver la documentación completa de cada script, uso y ejemplos.

## 📦 Requisitos
Python 3.8 o superior

psutil (pip install psutil)

Windows 10/11

Winget (preinstalado en Windows moderno)

## 🧠 Autor
Desarrollado por Antonio como parte de su toolkit técnico de automatización IT personal.