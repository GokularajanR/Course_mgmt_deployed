import uvicorn
from fastapi import FastAPI

from controllers.API_controller import app

main_api = FastAPI()
main_api.include_router(app)

if __name__ == "__main__":
    uvicorn.run("main:main_api")