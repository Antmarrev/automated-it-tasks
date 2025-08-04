@echo off
title automated-it-tasks - Instalación y ejecución
echo ====================================================
echo 🔧 automated-it-tasks - Instalación automatizada
echo ====================================================

:: Crear entorno virtual
echo.
echo [1/4] Creando entorno virtual...
python -m venv venv

:: Activar entorno virtual para este script (modo local)
echo.
echo [2/4] Activando entorno virtual...
call "%~dp0venv\Scripts\activate.bat"

:: Instalar dependencias
echo.
echo [3/4] Instalando dependencias desde requirements.txt...
"%~dp0venv\Scripts\python.exe" -m pip install --upgrade pip
"%~dp0venv\Scripts\python.exe" -m pip install -r requirements.txt

:: Ejecutar todos los scripts
echo.
echo [4/4] Ejecutando run_all.py...
"%~dp0venv\Scripts\python.exe" run_all.py

echo.
echo ✅ Todo completado.
pause
