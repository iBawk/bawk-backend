from fastapi import FastAPI
from routes import routes

app = FastAPI()

app.include_router(routes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', port=3334, reload=True)