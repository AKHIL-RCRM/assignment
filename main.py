from fastapi import FastAPI, UploadFile
import shutil
import extract as ex

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open('test.pdf', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    d = ex.extract_file()
    return {"filename": file.filename, 'output': d}
