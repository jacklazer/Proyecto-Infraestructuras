from locust import HttpUser, TaskSet, task, between
import json
import random
import string

class UserBehavior(TaskSet):

    def on_start(self):
        """ Called when a Locust start before any task is scheduled """
        self.proyecto_id = None

    @task(1)
    def inicio(self):
        self.client.get("/")

    @task(2)
    def listar_proyectos(self):
        response = self.client.get("/proyectos/")
        if response.status_code == 200:
            proyectos = response.json()  # Assuming your API returns JSON response
            if proyectos:
                self.proyecto_id = random.choice(proyectos)['id']

    @task(3)
    def ver_proyecto(self):
        if self.proyecto_id:
            self.client.get(f"/proyecto/{self.proyecto_id}/")

    @task(4)
    def crear_proyecto(self):
        try:
            # Obtener el token CSRF de la página de creación de proyecto (adaptar según tu estructura de HTML)
            response = self.client.get('/proyecto/nuevo/')
            csrf_token = response.cookies['csrftoken']

            # Datos del formulario para la creación de un proyecto
            data = {
                'nombre': 'Nuevo Proyecto',
                'descripcion': 'Descripción del nuevo proyecto',
                'csrfmiddlewaretoken': csrf_token,  # Incluir el token CSRF en la solicitud
            }

            # Realizar la solicitud POST con el token CSRF
            response = self.client.post('/proyecto/nuevo/', data=data, headers={'X-CSRFToken': csrf_token})

            # Manejo de la respuesta
            if response.status_code == 200:
                print("Proyecto creado exitosamente!")
            else:
                print(f"Error al crear proyecto. Código de estado: {response.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud POST: {e}")

    @task(5)
    def editar_proyecto(self):
        try:
            # Suponiendo que tienes un proyecto existente con ID conocido para editar
            proyecto_id = 1  # ID del proyecto a editar (ajusta según tus necesidades)
            
            # Realizar la solicitud GET para obtener el formulario de edición y el token CSRF
            response_get = self.client.get(f'/proyecto/{proyecto_id}/editar/')
            csrf_token = response_get.cookies['csrftoken']

            # Datos del formulario para la edición del proyecto (ajusta según tus necesidades)
            data = {
                'nombre': 'Proyecto Editado',
                'descripcion': 'Descripción actualizada del proyecto',
                'csrfmiddlewaretoken': csrf_token,  # Incluir el token CSRF en los datos de la solicitud
            }

            # Realizar la solicitud POST para editar el proyecto
            response_post = self.client.post(f'/proyecto/{proyecto_id}/editar/', data=data, headers={'X-CSRFToken': csrf_token})

            # Manejo de la respuesta
            if response_post.status_code == 200:
                print(f"Proyecto con ID {proyecto_id} editado exitosamente!")
            else:
                print(f"Error al editar proyecto con ID {proyecto_id}. Código de estado: {response_post.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud POST para editar el proyecto: {e}")

    @task(6)
    def borrar_proyecto(self):
        try:
            # Suponiendo que tienes un proyecto existente con ID conocido para borrar
            proyecto_id = 1  # ID del proyecto a borrar (ajusta según tus necesidades)
            
            # Realizar la solicitud GET para confirmar el borrado del proyecto
            response = self.client.get(f'/proyecto/{proyecto_id}/borrar/')
            
            # Manejo de la respuesta
            if response.status_code == 200:
                print(f"Proyecto con ID {proyecto_id} borrado exitosamente!")
            else:
                print(f"Error al borrar proyecto con ID {proyecto_id}. Código de estado: {response.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud GET para borrar el proyecto: {e}")
            self.proyecto_id = None

    @task(7)
    def crear_tarea(self):
        try:
            # Suponiendo que tienes un proyecto existente con ID conocido para agregar una tarea
            proyecto_id = 1  # ID del proyecto al cual agregar la tarea (ajusta según tus necesidades)
            
            # Realizar la solicitud GET para obtener el formulario de nueva tarea
            response_get = self.client.get(f'/tarea/nueva/{proyecto_id}/')
            csrf_token = response_get.cookies['csrftoken']

            # Datos del formulario para la nueva tarea (ajusta según tus necesidades)
            data = {
                'nombre': 'Nueva Tarea',
                'descripcion': 'Descripción de la nueva tarea',
                'csrfmiddlewaretoken': csrf_token,  # Incluir el token CSRF en los datos de la solicitud
            }

            # Realizar la solicitud POST para crear la nueva tarea
            response_post = self.client.post(f'/tarea/nueva/{proyecto_id}/', data=data, headers={'X-CSRFToken': csrf_token})

            # Manejo de la respuesta
            if response_post.status_code == 200:
                print(f"Nueva tarea creada en el proyecto con ID {proyecto_id}!")
            else:
                print(f"Error al crear nueva tarea en el proyecto con ID {proyecto_id}. Código de estado: {response_post.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud POST para crear la tarea: {e}")

    @task(8)
    def editar_tarea(self):
        try:
            # Suponiendo que tienes una tarea existente con ID conocido para editar
            tarea_id = 1  # ID de la tarea a editar (ajusta según tus necesidades)
            
            # Realizar la solicitud GET para obtener el formulario de edición de la tarea
            response_get = self.client.get(f'/tarea/{tarea_id}/editar/')
            csrf_token = response_get.cookies['csrftoken']

            # Datos del formulario para la edición de la tarea (ajusta según tus necesidades)
            data = {
                'nombre': 'Tarea Editada',
                'descripcion': 'Descripción actualizada de la tarea',
                'csrfmiddlewaretoken': csrf_token,  # Incluir el token CSRF en los datos de la solicitud
            }

            # Realizar la solicitud POST para editar la tarea
            response_post = self.client.post(f'/tarea/{tarea_id}/editar/', data=data, headers={'X-CSRFToken': csrf_token})

            # Manejo de la respuesta
            if response_post.status_code == 200:
                print(f"Tarea con ID {tarea_id} editada exitosamente!")
            else:
                print(f"Error al editar tarea con ID {tarea_id}. Código de estado: {response_post.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud POST para editar la tarea: {e}")

    @task(9)
    def borrar_tarea(self):
        try:
            # Suponiendo que tienes una tarea existente con ID conocido para borrar
            tarea_id = 1  # ID de la tarea a borrar (ajusta según tus necesidades)
            
            # Realizar la solicitud GET para confirmar el borrado de la tarea
            response = self.client.get(f'/tarea/{tarea_id}/borrar/')
            
            # Manejo de la respuesta
            if response.status_code == 200:
                print(f"Tarea con ID {tarea_id} borrada exitosamente!")
            else:
                print(f"Error al borrar tarea con ID {tarea_id}. Código de estado: {response.status_code}")

        except Exception as e:
            print(f"Error al realizar la solicitud GET para borrar la tarea: {e}")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://localhost:8000"  # Configura el host aquí
