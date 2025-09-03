# ETL para Procesamiento de Datos con IA

Este proyecto implementa un proceso ETL (Extract, Transform, Load) diseñado para obtener 
información de fuentes externas, procesarla utilizando limpieza de datos, y almacenar 
los resultados en un bucket de S3 con caché en CDN para un acceso rápido.

## 🚀 Descripción del Proyecto

El ETL se encarga de:
1. **Extraer** datos de fuentes externas
2. **Transformar** los datos para solo utilizar los que se necesitan y limpiar valores nulos
3. **Cargar** los resultados procesados en un bucket de S3
4. Gestionar la caché en CDN para un acceso rápido a los datos procesados

## 🛠 Configuración del Entorno

### 1) 📦 Crear el entorno virtual

Un entorno virtual aísla las dependencias de tu proyecto, evitando conflictos con otras instalaciones de Python.

```bash
python -m venv .venv
```

### 2) ▶️ Activar el entorno virtual

- **Windows (PowerShell)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (CMD)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **macOS/Linux (Bash/Zsh)**:
  ```bash
  source .venv/bin/activate
  ```
- **macOS/Linux (Fish)**:
  ```fish
  source .venv/bin/activate.fish
  ```

### 3) 🐍 Verificar la versión de Python

```bash
# Windows
.\.venv\Scripts\python.exe --version

# macOS/Linux
.venv/bin/python --version
```

### 4) ⚙️ Actualizar pip

```bash
python -m pip install --upgrade pip
```

### 5) ✨ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6) 🔑 Configurar variables de entorno

Crea el archivo de configuración con el siguiente comando:

```bash
python -m scripts.setup_secrets
```

Este script te guiará en la configuración de los secretos necesarios, como los recursos de AWS para S3 y CloudFront.

### 7) 🚦 Ejecución del ETL

### Descarga y procesamiento de datos

```bash
python -m scripts.load_dataset
```

### Entrenar modelo de ML

```bash
python -m scripts.train_models
```

### Subida a S3

```bash
python -m scripts.upload_s3
```

### Invalidar caché del CDN (si es necesario)

```bash
python -m scripts.invalidate_cache
```

---

## 📁 Estructura del Proyecto

- `scripts/`: Contiene todos los scripts de Python para el proceso ETL
  - `load_dataset.py`: Descarga y prepara los datos de origen
  - `train_models.py`: Entrena los modelos de IA
  - `upload_s3.py`: Maneja la carga de archivos a S3
  - `invalidate_cache.py`: Gestiona la invalidación de la caché del CDN
  - `setup_secrets.py`: Configura las variables de entorno necesarias
- `dto/`: Contiene los modelos de datos utilizados en el proyecto
- `utils/`: Utilidades y helpers para el proyecto

## 🔄 Flujo de Trabajo

1. Los datos son extraídos de kaggle y se cachean en tu equipo para reutilizarlos en futuras ejecuciones
2. Se aplican transformaciones utilizando limpieza profunda y usando solo propiedades requeridas
3. Los resultados se almacenan localmente para validación
4. Los archivos procesados se suben a S3
5. Se configura la caché del CDN para un acceso rápido

## 📝 Notas Adicionales

- Asegúrate de tener configuradas las credenciales de AWS con los permisos necesarios para S3 y CloudFront
- El proceso de invalidación de caché puede tardar hasta 15 minutos en propagarse completamente
