# Proyecto-Infraestructuras

## Cómo ejecutar el proyecto localmente

### Paso 1: Clonar el repositorio

git clone https://github.com/jacklazer/Proyecto-Infraestructuras.git

### Paso 2: Crear un ambiente virtual

python -m venv nombre_del_ambiente

### Paso 3: Activar el ambiente virtual

nombre_del_ambiente\Scripts\activate  # En Windows
source nombre_del_ambiente/bin/activate  # En macOS/Linux

### Paso 4: Ingresar a la carpeta raíz del proyecto

cd gestion_tareas

### Paso 5: Instalar los requerimientos

pip install -r requirements_complete_version.txt

### Paso 6: Ejecutar el proyecto

python manage.py runserver

### Paso 7: Acceder a la aplicación

Ingresar a la aplicación a través de http://127.0.0.1:8000/

Nota importante: Para ejecutar el proyecto con `python manage.py runserver`, verifica que en el archivo `settings.py` esté descomentada la línea 96 y comentada la línea 97. Para desplegar con Docker Swarm, debe ser al revés.

---

## Cómo desplegar el proyecto con Docker Swarm

### Paso 1: Clonar el repositorio

git clone https://github.com/jacklazer/Proyecto-Infraestructuras.git

### Paso 2: Ingresar a la carpeta raíz del proyecto

cd gestion_tareas

### Paso 3: Construir la imagen de Docker

docker build -t my_django_app .

### Paso 4: Inicializar un nodo en Docker Swarm

docker swarm init

### Paso 5: Desplegar servicios con Docker Compose en Docker Swarm

docker stack deploy -c docker-compose.yml my_stack

### Paso 6: Ver los contenedores en ejecución

docker ps

### Paso 7: Copiar el resto del nombre del contenedor necesario

# Utiliza este nombre en el Paso 8

### Paso 8: Ejecutar migraciones dentro del contenedor

docker exec -it my_stack_web.1.<resto_del_nombre_del_contenedor> python manage.py migrate

### Paso 9: Acceder a la aplicación

Ingresar a la aplicación a través de http://127.0.0.1:8000/

Nota importante: Para desplegar con Docker Swarm, verifica que en el archivo `settings.py` esté descomentada la línea 97 y comentada la línea 96. Para ejecutar el proyecto localmente, debe ser al revés.

---

## Cómo hacer pruebas con Locust

### Paso 1: Desplegar o ejecutar el proyecto

### Paso 2: En una terminal diferente:

#### Paso 2.1: Activar el ambiente virtual

nombre_del_ambiente\Scripts\activate  # En Windows
source nombre_del_ambiente/bin/activate  # En macOS/Linux

#### Paso 2.2: Ingresar a la carpeta raíz del proyecto

cd gestion_tareas

#### Paso 2.3: Iniciar Locust

locust -f locustfile.py

### Paso 3: Acceder a Locust

Ingresar a Locust a través de http://localhost:8089

### Paso 4: Configurar y ejecutar la prueba

Configura `Number of users`, `Ramp up`, y haz clic en el botón START
