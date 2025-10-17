from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Перейдите на /file чтобы получить файл."}


@app.get("/file")
async def get_file():
    return FileResponse("message.txt", media_type="text/plain", filename="message.txt")
