
from datetime import datetime
from fastapi import FastAPI
import socket
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="FastAPI App")

hostname = socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

now = datetime.now()
unique_id = str(uuid4())

@app.get("/")
async def info():
    return {"Date and time": now, "id": unique_id, "Hostname": hostname, "IP": IPAddr}
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Instrumentator().instrument(app).expose(app)
