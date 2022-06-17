from fastapi import APIRouter, Depends

from ..database import crud, schemas
from ..dependencies import get_db
from ..funcs import counter


router = APIRouter(prefix="/color", tags=["Color"])


@router.get('/{index}/')
async def read_messages(index: int, db=Depends(get_db)):
    return {"result": crud.get_color_by_id(db, index)}
