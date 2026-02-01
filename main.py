# Importing Modules
from fastapi import FastAPI
import secrets
import string
import random

app = FastAPI()

@app.get("/generate-password")
# Defining Create_Strong_Password Function
def generate_password(length: int = 13):
    # Assigning Attributes for Password
    attributes = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    # Creating the full password
    password = "".join(secrets.choice(attributes) for _ in range(length))

    return "".join(password)