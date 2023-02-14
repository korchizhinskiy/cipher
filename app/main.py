from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from app.decipher import get_list_with_deciphered_words

app = FastAPI()


@app.get("/")
def send_form():
    return FileResponse("./app/template/cipher.html")


@app.post("/post_decipher")
def read_cipher(cipher: str = Form()):
    words_after_decipher = get_list_with_deciphered_words(cipher)
    return {"Deciphered words": words_after_decipher}
