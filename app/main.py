import ldclient
import sys
from fastapi import FastAPI

app = FastAPI()

version = f"{sys.version_info.major}.{sys.version_info.minor}"

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn in Alpine. Using Python {version}"
    return {"message": message}

print("it worked!")
