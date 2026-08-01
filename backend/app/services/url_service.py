from sqlalchemy.orm import Session

from app.models.url import URL
from app.schemas.url import URLCreate, URLResponse
from app.utils.generator import generate_short_code


def create_short_url(
    db: Session,
    data: URLCreate
) -> URLResponse:

    short_code = generate_short_code()

    url = URL(
        short_code=short_code,
        original_url=str(data.url)
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return URLResponse(
        short_code=url.short_code,
        short_url=f"http://localhost:8000/{url.short_code}"
    )

from fastapi import HTTPException


def get_original_url(
    db: Session,
    short_code: str
) -> URL:

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if url is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return url