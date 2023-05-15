from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/test")
def read_root():
    return {"Test endpoint"}

@app.get("/submitbutton")
def read_root():
    return {"Thanks for clicking"}

@app.get("/subtraction")
def read_root():
    return {"Subtraction endpoint"}


