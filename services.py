from datetime import datetime
from utils import generate_shortcode, is_valid_url
from errors import InvalidRequestError, ConflictError
from models import Url
from storage import get_url_by_shortcode, save_url, delete_url

MAX_RETRIES = 5

def create_short_url(original_url:str)->Url:
    if not is_valid_url(original_url):
        raise InvalidRequestError(
            message = "Invalid URL format",
            details = {"url":"Must be a valid HTTP or HTTPS URL"},
        )
    
    for _ in range(MAX_RETRIES):
        short_code = generate_shortcode()
        existing = get_url_by_shortcode(short_code)
        if not existing:
            break
    else:
        raise ConflictError(
            message = "Failed to generate unique shortcode",
        )
    now = datetime.utcnow()
    url = Url(
        original_url=original_url,
        short_code = short_code,
        created_at= now,
        access_count=0,
        updated_at= now,
    )
    save_url(url)
    return url

def delete_short_url(short_code:str)->None:
    existing = get_url_by_shortcode(short_code)
    if not existing:
        raise InvalidRequestError(
            message = "Shortcode does not exist"
        )
    delete_url(existing)

