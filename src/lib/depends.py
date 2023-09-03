from fastapi import Depends
from db.connection import Session

def get_db_Session():
    try:
        session = Session()
        yield session
    finally:
        session.close()