from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Lambda!"}

@app.get("/testing")
async def testing():
    return {"message": "Testing, Lambda!"}


handler = Mangum(app)