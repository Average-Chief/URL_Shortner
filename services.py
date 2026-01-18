from datetime import datetime
from utils import generate_shortcode, is_valid_url
from errors import InvalidRequestError, ConflictError
from models import Url
from storage import get_url_by_shortcode, save_url

MAX_RETRIES = 5

def create_short_url(original_url:str)->str:
    if not is_valid_url(original_url):
        raise InvalidRequestError(
            message = "Invalid URL format",
            details = {"url":"Must be a valid HTTP or HTTPS URL"},
        )
    
    for _ in range(MAX_RETRIES):
        short_code = generate_shortcode()
        exisiting = get_url_by_shortcode(short_code)
        if not exisiting:
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
    return short_code