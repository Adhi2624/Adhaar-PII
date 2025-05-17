from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
import os
import shutil
from parser import ocrReader
from ollamaClient import OllamaClient
import json
from PIL import Image
from PIL import ImageDraw
import base64
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
imageParserClient=ocrReader()
OllamaClient=OllamaClient()
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)
    
def MaskAndBase64(filepath, string):
    img = Image.open(filepath).convert("RGB")
    print(img.format)
    draw = ImageDraw.Draw(img)
    draw.text((28, 36), string, fill=(255, 0, 0))
    img.save(filepath, format='JPEG')
    with open(filepath, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        base64_string = encoded_bytes.decode('utf-8')
        return base64_string   
    

@app.post('/upload')
async def upload_file(file: UploadFile = File(...), type: str = Form(...)):
    fileName=file.filename.replace(' ', '')
    file_name = f"{uuid4()}_{fileName}"
    file_location = os.path.join(UPLOAD_DIR, file_name)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    parserText=''
    fileExtension=file.filename.split('.')[-1]
    maskedimg=''
    if (type=='application/pdf' or fileExtension=='pdf'): 
        parserText=imageParserClient.readTextfromPdf(filePath=file_location)
        file_location=parserText[0]
        parserText=parserText[1]
    else:
        parserText=imageParserClient.readTextfromImage(file_location)
        
    try:
        parsedData=OllamaClient.askOllama(parserText)
        maskedimg=MaskAndBase64(file_location,parsedData)
    except Exception as e:
        print(e)
        return {
            "message":f"LLms Not found {e}"
        }
    os.remove(file_location)
    return {parsedData,parserText,maskedimg}
