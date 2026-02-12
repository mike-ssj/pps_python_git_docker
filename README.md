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

## Ejecución de la Aplicación (Con Docker Compose) **RECOMENDADO**
Esta opción es la más sencilla, pero hay que tener docker-compose instalado:

```docker-compose up --build```

## Ejecución de la Aplicación (Con Docker Estándar)
Para crear todos los contenedores manualmente, se puede hacer con los siguientes comandos:
```
sudo docker network create bayeta-net

sudo docker run -d --name mongodb --network bayeta-net mongo

sudo docker build -t bayeta .
sudo docker run -d --name bayeta --network bayeta-net -p 5000:5000 bayeta
```

## Ejecución de la Aplicación (Sin Docker)

Si se quiere lanzar la app sin docker:

```python app.py```


## Acceso a la aplicación

### Abrir en el navegador:
```http://localhost:5000```

(No había leído toda la práctica e implementé docker compose en la rama de mongodb por comodidad -.-")