# Procedimiento para ejecutar los ejercicios del taller

## Requisitos previos
- Python
- Git
- Clave de acceso a la API de Gemini

## Instrucciones de ejecución (Windows)

### Paso 1: Clonar repositorio

En la terminal:
```bash
git clone https://github.com/sxmuxel/TallerGenAI.git
cd TallerGenAI
```

### Paso 2: Crear entorno virtual

En la terminal:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Paso 3: Instalar dependencias

En la terminal:
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la variable de entorno

Crear un archivo .env en la raíz del proyecto a partir del archivo de ejemplo.

En la terminal:
```bash
copy .env.example .env
```
Reemplazar la clave genérica por la clave propia.

### Paso 5: Ejecutar los ejercicios del taller

En la terminal:

Para Ejercicio #1 - Conexión y Petición Básica: 
```bash
python ejercicio_peticion.py
```

Para Ejercicio #2 - Procesador de Textos Inteligente: 
```bash
python ejercicio_procesador.py
```

Para Ejercicio #3 - Chat de Soporte con Historial: 
```bash
python ejercicio_chat_soporte.py
```
