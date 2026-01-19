from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from services import (
    create_short_url,
    get_short_url,
    update_short_url,
    delete_short_url,
    redirect_short_url,
    get_url_stats,
)
from errors import InvalidRequestError, ConflictError
from schemas import CreateUrlRequest, UpdateUrlRequest

router = APIRouter(prefix="/shorten")


@router.post("")
def shorten_url(payload: CreateUrlRequest):
    try:
        return create_short_url(payload.url)
    except InvalidRequestError as e:
        raise HTTPException(status_code=400, detail=e.message)
    except ConflictError as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("/{short_code}")
def get_url(short_code: str):
    try:
        return get_short_url(short_code)
    except InvalidRequestError as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{short_code}")
def update_url(short_code: str, payload: UpdateUrlRequest):
    try:
        return update_short_url(short_code, payload.url)
    except InvalidRequestError as e:
        raise HTTPException(status_code=400, detail=e.message)


@router.delete("/{short_code}", status_code=204)
def delete_url(short_code: str):
    try:
        delete_short_url(short_code)
    except InvalidRequestError as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/{short_code}/stats")
def url_stats(short_code: str):
    try:
        return get_url_stats(short_code)
    except InvalidRequestError as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/r/{short_code}")
def redirect_url(short_code: str):
    try:
        destination = redirect_short_url(short_code)
        return RedirectResponse(url=destination, status_code=302)
    except InvalidRequestError as e:
        raise HTTPException(status_code=404, detail=e.message)
