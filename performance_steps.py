
import random
from behave import given, when, then
import requests

BASE_URL = "http://127.0.0.1:5000"

@given("I have random registration data")
def step_random_data(context):
    context.data = {
        "fullName": f"User{random.randint(1, 10000)}",
        "userName": f"user{random.randint(1, 10000)}",
        "email": f"user{random.randint(1, 10000)}@example.com",
        "password": "password123",
        "phone": str(random.randint(1000000000, 9999999999))
    }

@given("I have valid login credentials")
def step_login_data(context):
    context.data = {
        "userName": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }

@when('I send a POST request to "{endpoint}"')
def step_post_request(context, endpoint):
    url = f"{BASE_URL}{endpoint}"
    context.response = requests.post(url, data=context.data)

@then("I should get a 200 response")
def step_validate_response(context):
    assert context.response.status_code == 200
