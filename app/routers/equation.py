from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..database import schemas
from ..funcs import counter


router = APIRouter(prefix="/equation", tags=["Equation"])


@router.post('/')
async def read_messages(data: schemas.Numbers):
    if data.a != 0 and data.b != 0 and data.c != 0:
        return {"result": counter(data)}
    else:
        return JSONResponse({"result": "division by zero"}, status_code=422)
