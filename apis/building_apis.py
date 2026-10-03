from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greeting():
    return {"message": "Welcome to the Building APIs!"}

@app.get("/buildings")
def get_buildings():
    # Placeholder for fetching building data
    buildings = [
        {"id": 1, "name": "Building A", "location": "City Center"},
        {"id": 2, "name": "Building B", "location": "Uptown"},
    ]
    return {"buildings": buildings}

@app.get("/buildings/{building_id}")
def get_building(building_id: int):
    # Placeholder for fetching a specific building by ID
    building = {"id": building_id, "name": f"Building {building_id}", "location": "Unknown"}
    return {"building": building}

@app.get("/greet/{username}")
def greet_user(username: str):
    return {"message": f"Hello, {username}!"}

@app.get("/greet/{username}")
def greet_user_path(username: str):
    return {"message": f"Hello, {username}!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

