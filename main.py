from fastapi import FastAPI, File, UploadFile
import shutil
import extract as ex

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open('test.pdf', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    d = ex.extract_file()
    return {"filename": file.filename, 'output': d}

