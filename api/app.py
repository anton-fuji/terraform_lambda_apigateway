from fastapi import FastAPI, Request
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, Lambda!"}

@app.get("/testing")
async def testing():
    return {"message": "Testing, Lambda!"}

@app.get("/{proxy_path:path}")
async def catch_all(proxy_path: str, request: Request):
    return {
        "proxy_path": proxy_path,
        "full_path": str(request.url.path),
        "query_params": dict(request.query_params),
        "headers": dict(request.headers)
    }
    
    
handler = Mangum(app)