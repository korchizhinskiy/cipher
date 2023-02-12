from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.cipher import decipher_word

app = FastAPI()


@app.get("/")
def send_form():
    return FileResponse("./app/template/cipher.html")


@app.post("/post_cipher")
def read_cipher(cipher: str = Form()):
    words_after_decipher = decipher_word(cipher)
    return {"cipher": words_after_decipher}
