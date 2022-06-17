from fastapi import APIRouter, Depends

from ..database import crud, schemas
from ..dependencies import get_db
from ..funcs import counter


router = APIRouter(prefix="/equation", tags=["Equation"])


@router.post('/')
async def read_messages(data: schemas.Numbers, db=Depends(get_db)):
    return {"result": counter(data)}
