from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=3334)