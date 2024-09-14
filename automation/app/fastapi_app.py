from fastapi import FastAPI
from app.api.v1 import bind_routers


app = FastAPI()
app.include_router(bind_routers)