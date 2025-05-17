from parser import ocrReader
client=ocrReader()
a=r'D:\projects\Adhaar-PII\fgs.jpg'
parsedText=client.readTextfromImage(filePath=a)


from main import MaskAndBase64
MaskAndBase64(a,"hello")