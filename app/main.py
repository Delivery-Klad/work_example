from fastapi import FastAPI, Request, Response

from migrate import automigrate
from sqlalchemy.orm import Session

from app.database import crud
from app.database.database import SessionLocal, engine
from app.dependencies import get_settings
from app.routers import equation, color


settings = get_settings()

app = FastAPI()
app.include_router(equation.router)
app.include_router(color.router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.on_event("startup")
def startup_event():
    automigrate()
    with Session(engine) as db:
        crud.set_colors(db)
