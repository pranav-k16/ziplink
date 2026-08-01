from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.url import URLCreate, URLResponse
from app.services.url_service import create_short_url

from fastapi.responses import RedirectResponse

from app.services.url_service import (
    create_short_url,
    get_original_url
)



router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
def shorten_url(
    data: URLCreate,
    db: Session = Depends(get_db)
):
    return create_short_url(db, data)

@router.get("/{short_code}")
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db)
):

    url = get_original_url(db, short_code)

    return RedirectResponse(url.original_url)