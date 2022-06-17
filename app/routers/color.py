from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..database import crud
from ..dependencies import get_db


router = APIRouter(prefix="/color", tags=["Color"])


@router.get('/{index}/')
async def read_messages(index: int, db=Depends(get_db)):
    result = crud.get_color_by_id(db, index)
    if result is not None:
        return {"result": result}
    else:
        return JSONResponse(status_code=404)
