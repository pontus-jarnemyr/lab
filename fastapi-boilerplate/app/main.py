from __future__ import annotations
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .database import Base, engine
from .api.v1.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users_router, prefix="/api/v1")

@app.get("/")
def read_root(request: Request):
    base_url = f"{request.url.scheme}://{request.url.netloc}"
    return JSONResponse(content={"message": f"Server is running! For API docs, visit {base_url}{app.docs_url}"})


@app.get("/api/healthcheck")
def healthcheck():
    return JSONResponse(content={"message": "Server is running!"})
