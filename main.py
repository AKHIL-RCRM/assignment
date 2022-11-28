from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open('test.pdf', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

