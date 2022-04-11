from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.Game import Game
import os
import secrets


class Mission(BaseModel):
    """Mission object"""
    script: str


NASA_USER = os.environ["NASA_USER"]
NASA_PASS = os.environ["NASA_PASS"]

app = FastAPI()  # starting API
security = HTTPBasic()


@app.get("/")
def home():
    """
        Home route, redirected to path /mission
    :return: (JSONResponse) -> Result of the script
    """
    return RedirectResponse("/mission")


@app.get("/mission")
def process_mission(mission: Mission, credentials: HTTPBasicCredentials = Depends(security)):
    """
        Returns the result of the execution of the plateau initialization and rover movement script
    :param mission: (Mission) -> Mission object containing the script to be executed \n
    :param credentials: (HTTPBasicCredentials) -> Basic auth to api \n
    :return: (JSONResponse) -> Result of the script
    """
    correct_username = secrets.compare_digest(credentials.username, NASA_USER)
    correct_password = secrets.compare_digest(credentials.password, NASA_PASS)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    g1 = Game(mission.script)  # Game initialization
    result_json = jsonable_encoder(g1.start())  # Getting result of the script execution
    status_code = status.HTTP_200_OK
    return JSONResponse(status_code=status_code, content=result_json)
