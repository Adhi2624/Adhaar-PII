from openai import OpenAI
import time

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
a=time.time()
data="""Adhithiyan
S/O: Ravi
112/2
KATTUKOTTAY
Sadaiyampattu
Viluppuram Tamil Nadu - 606213
7339527989
2138 9892 0523
VID : 9182 4460 1645 5696
Download Date: 15/11/2023
Issue Date: 21/09/2013
ஆ
ய

Adhithiyan
றத நா/DOB: 02/06/2004
/ MALE
2138 9892 0523
VID : 9182 4460 1645 5696
கவ:
S/O: ர, 112/2, காெகாடா,
சைடயப,  !"ர,
த#$ நா - 606213
Address:
S/O: Ravi, 112/2, KATTUKOTTAY,
Sadaiyampattu, Viluppuram,
Tamil Nadu - 606213
2138 9892 0523
VID : 9182 4460 1645 5696
Digitally signed by DS
UNIQUE IDENTIFICATION
AUTHORITY OF INDIA 05
Date: 2023.11.15 10:54:22
UTC
Signature Not Verified

பேவ / Enrolment No.: 0651/60142/62022
To
ஆ
ய

Adhithiyan
S/O: Ravi
112/2
KATTUKOTTAY
Sadaiyampattu
Viluppuram Tamil Nadu - 606213
7339527989
2138 9892 0523
VID : 9182 4460 1645 5696
Download Date: 15/11/2023
Issue Date: 21/09/2013
ஆ
ய

Adhithiyan
றத நா/DOB: 02/06/2004
/ MALE
2138 9892 0523
VID : 9182 4460 1645 5696
கவ:
S/O: ர, 112/2, காெகாடா,
சைடயப,  !"ர,
த#$ நா - 606213
Address:
S/O: Ravi, 112/2, KATTUKOTTAY,
Sadaiyampattu, Viluppuram,
Tamil Nadu - 606213
2138 9892 0523
VID : 9182 4460 1645 5696
Digitally signed by DS
UNIQUE IDENTIFICATION
AUTHORITY OF INDIA 05
Date: 2023.11.15 10:54:22
UTC
Signature Not Verified"""
completion = client.chat.completions.create(
  model="google/gemma-3-12b-it:free",
  messages=[
    {
                    'role': "system",
                    'content': """
        You are an AI agent who is Instructed to Work on Aadhaar card data.
        Your task is to extract personal identification information from the provided input and return it in the following JSON format:

        {
        "name": "",
        "address": "",
        "dob": "",
        "aadhaarNumber": "",
        "phoneNumber": ""
        }

        Instructions:
        - If any specific information is missing or not found, leave its value as an empty string.
        - The Aadhaar number is a 12-digit number and may be formatted as three blocks of four digits (e.g., 1234 5678 9012). It typically appears near the address.
        - The date of birth (dob) can be in formats like DD/MM/YYYY or MM/YYYY.
        - The phone number is usually a 10-digit number and may be labeled as "Mobile" or "Phone".

        Return only the JSON output — no explanations or additional text.
        """
                    },
                    {
                        'role': 'user',
                        'content': str(data)
                    }
  ]
)

print(completion.choices[0].message.content)
print(time.time()-a)