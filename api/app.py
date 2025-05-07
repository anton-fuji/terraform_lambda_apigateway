from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api")
async def home():
    return {"message": "Hello, Lambda!"}

@app.get("/api/testing")
async def testing():
    return {"message": "Testing, Lambda!"}


handler = Mangum(app)