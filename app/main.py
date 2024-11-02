from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
