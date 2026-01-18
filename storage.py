from models import Url
from db import engine
from sqlmodel import Session, select

def get_url_by_shortcode(short_code:str)->Url|None:

    with Session(engine) as session:
        stmt = select(Url).where(Url.short_code == short_code)
        result = session.exec(stmt).first()
        return result

def save_url(url:Url)->None:
    try:
        with Session(engine) as session:
            session.add(url)
            session.commit()
            session.refresh(url)
    except Exception as e:
        raise e


def delete_url(url:Url)->None:
    with Session(engine) as session:
        session.delete(url)
        session.commit()

