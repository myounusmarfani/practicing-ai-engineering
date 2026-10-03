## Creating an API for user authentication and authorization, saving the user into the json file

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import json

app = FastAPI(
    title="User Authentication API",
    description="An API for user authentication and authorization"
)

# Define a Pydantic model for user data
class User(BaseModel):
    username: str
    password: str
    age: int

# Define a function to load users from a JSON file
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Define a function to save users to a JSON file
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Define an endpoint to register a new user
@app.post("/register")
def register_user(user: User):
    users = load_users()
    # Check if the username already exists
    if any(u["username"] == user.username for u in users):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Add the new user to the list and save it
    users.append(user.dict())
    save_users(users)
    return {"message": "User registered successfully"}


# Define an endpoint to authenticate a user
@app.post("/login")
def login_user(user: User):
    users = load_users()
    # Check if the username and password match
    for u in users:
        if u["username"] == user.username and u["password"] == user.password:
            return {"message": "Login successful"}
    
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Define an endpoint to get all registered users (for demonstration purposes)
@app.get("/users")
def get_users():
    users = load_users()
    return {"users": users}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)