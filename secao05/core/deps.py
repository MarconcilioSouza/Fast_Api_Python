from typing import AsyncGenerator

from core.database import Session

async def get_session() -> AsyncGenerator:
    session = Session()
    try:
        yield session
    finally:
        session.close()