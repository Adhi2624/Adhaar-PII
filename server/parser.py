import easyocr
import pymupdf
import os
from pdf2image import convert_from_path
from PIL import Image
class ocrReader():
    def __init__(self):
        self.reader=easyocr.Reader(['en'])
    def readTextfromImage(self,filePath:str):
        res=self.reader.readtext(filePath,detail=0)
        res='\n'.join(res)
        return res
    def readTextfromPdf(self,filePath:str):
        NewImgPath=''
        retrivedtext=''
        try:
            images = convert_from_path(filePath,poppler_path=r'C:\Users\adhia\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin')
            NewImgPath=filePath.split('.')[0]+'.jpg'
            for i, image in enumerate(images):
                image.save(NewImgPath, 'JPEG')
                retrivedtext=self.readTextfromImage(NewImgPath)
        except Exception as e:
                print(f"An error occurred: {e}")
        return [NewImgPath,retrivedtext]

