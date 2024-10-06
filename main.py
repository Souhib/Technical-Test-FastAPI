from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.app import create_app
from api.database import create_app_engine, create_db_and_tables


from load_picture import store_frames_sqlmodel

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_app_engine()
    create_db_and_tables(engine)
    try:
        store_frames_sqlmodel("img.csv", engine)
    except IntegrityError:
        pass
    except Exception as e:
        print(e)
        raise e
    engine.dispose()
    yield


app = create_app(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
