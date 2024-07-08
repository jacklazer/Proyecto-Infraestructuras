from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def view_projects(self):
        self.client.get("/proyectos/")

    # @task(3)
    # def create_project(self):
    #     self.client.post("/proyectos/", json={"name": "Nuevo Proyecto", "description": "Descripción del proyecto"})

    # @task(4)
    # def cause_error(self):
    #     self.client.get("/invalid-url")  # Un URL que no existe para causar un error 404

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://localhost:8000"  # Configura el host aquí
