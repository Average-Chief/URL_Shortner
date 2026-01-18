import string 
import secrets
from urllib.parse import urlparse

_SHORTCODE_CHARS = string.ascii_letters + string.digits
_SHORTCODE_LENGTH = 6

def generate_shortcode()->str:
    return ''.join(secrets.choice(_SHORTCODE_CHARS) for _ in range(_SHORTCODE_LENGTH))

def is_valid_url(url:str)->bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in ('http','https') and bool(parsed.netloc)
    except Exception:
        return False