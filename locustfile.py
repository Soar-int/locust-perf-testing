
from locust import HttpUser, task, between
import random

class LoadTesting(HttpUser):
    wait_time = between(1, 5)

    @task
    def client_register(self):
        self.client.post("/client_registeration", data={
            "fullName": "Test User",
            "userName": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "phone": "1234567890"
        })

class StressTesting(HttpUser):
    wait_time = between(1, 2)

    @task
    def client_login(self):
        self.client.post("/client_login", data={
            "userName": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        })
