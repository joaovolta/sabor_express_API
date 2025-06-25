# pip install fastapi
# pip install uvicorn
# uvicorn "nomedoarquivo":app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")

def hello():
    return {"Hello":"World"}