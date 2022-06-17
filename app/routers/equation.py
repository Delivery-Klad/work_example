from fastapi import APIRouter

from ..database import schemas
from ..funcs import counter


router = APIRouter(prefix="/equation", tags=["Equation"])


@router.post('/')
async def read_messages(data: schemas.Numbers):
    return {"result": counter(data)}
