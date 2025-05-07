from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Lambda!"}

@app.get("/testing")
def testing():
    return {"message": "Testing, Lambda!"}
