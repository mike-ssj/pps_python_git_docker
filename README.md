# La Bayeta de la Fortuna
“La Bayeta de la Fortuna” es una aplicación web sencilla que muestra un mensaje auspicioso aleatorio cada vez que accedes a ella. Está inspirada en las galletas de la fortuna y diseñada para ser fácil de ejecutar y mantener.





## Instalación


### 1. Clonar el repositorio
```git clone https://github.com/mike-ssj/pps_python_git_docker.git```

```cd pps_python_git_docker```

### 2. Crear el Entorno Virtual
Para evitar conflictos con otras librerías de tu sistema, creamos un entorno aislado:

```python -m venv env```

### 3. Activar el Entorno Virtual
Antes de instalar nada, activa el entorno:

```source venv/bin/activate```

### 4. Resolución de Dependencias
Una vez activado el entorno, instala todas las librerías necesarias:

```pip install -r requirements.txt```

---

## Ejecución de la Aplicación (Sin Docker)

Una vez completada la instalación, puedes lanzar la aplicación:

```python app.py```

## Ejecución de la Aplicación (Con Docker)
### Construcción de la imagen Docker
```docker build -t bayeta-fortuna .```

### Ejecución del contenedor
```docker run -p 8000:5000 bayeta-fortuna```

## Acceso a la aplicación

### Abrir en el navegador: (Con Docker)
```http://localhost:8000```

### Abrir en el navegador: (Sin Docker)
```http://localhost:5000```