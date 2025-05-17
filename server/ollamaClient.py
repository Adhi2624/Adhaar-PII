import ollama

class OllamaClient():
    def __init__(self):
        self.client = ollama.Client(host='http://localhost:11434')

    def askOllama(self,data: str):
        print(data)
        res = self.client.chat(
            model='gemma3',
            messages=[
                {
                    'role': "system",
                    'content':"""
                    You are an AI agent assigned to extract personal identification information from Aadhaar card data.

Your task is to analyze the given Aadhaar card content and return the result in the following JSON format:

{
  "Name": "",
  "Address": "",
  "DOB": "",
  "AadhaarNumber": "",
  "PhoneNumber": ""
}

Strict Extraction Guidelines:

1. Missing Information:
   - If any field is missing or cannot be confidently identified, leave it as an empty string ("").

2. Aadhaar Number:
   - Must be a 12-digit number, either in one block or grouped as three blocks of four digits (e.g., "1234 5678 9012").
   - Located near the address or the text "Your Aadhaar No".
   - Ignore any 16-digit numbers (these are Virtual IDs, not Aadhaar numbers).
   - Ensure it is **not reused** as any other field value (e.g., PhoneNumber).

3. Date of Birth (DOB):
   - Acceptable formats: "DD/MM/YYYY" or "MM/YYYY".
   - Look near personal details like name, gender, or label "DOB".

4. Phone Number:
   - Must be a **10-digit number** (Indian mobile format).
   - Must be clearly labeled or appear right after the address section.
   - Do **not** use:
     - Aadhaar number (12 digits)
     - VID (16 digits)
     - Repeated Aadhaar number
   - If no 10-digit number is confidently identified as a phone number, leave it as an empty string ("").

Important Instructions:
- Do NOT infer or guess values.
- Only extract if the format and context are clearly correct.
- Return only the final JSON output — no explanations or extra content.

                    """
                    },
                    {
                        'role': 'user',
                        'content': str(data)
                    }
                ],
                stream=False,
                format='json'
            )
        return res['message']['content']
