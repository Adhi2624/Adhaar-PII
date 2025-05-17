# Adhaar Data PII Masking Application

## Description

This application allows users to upload Aadhaar card images or PDFs, extract personal identification information (PII), mask the PII in the image, and display the extracted data in a structured format.

## Features

*   Upload Aadhaar card images or PDFs.
*   Extract text from the uploaded file using OCR.
*   Identify and extract PII such as Name, Address, Date of Birth, Aadhaar Number, and Phone Number using an AI model.
*   Mask the extracted PII in the uploaded image.
*   Display the extracted PII in a table.
*   Display the masked image.

## Technologies Used

*   Frontend: React, Axios
*   Backend: FastAPI, Uvicorn
*   OCR: easyocr
*   AI Model: Ollama (gemma3)
*   PDF Processing: pymupdf, pdf2image

## Backend Files Explanation

*   `main.py`: This file contains the main FastAPI application. It handles file uploads, calls the OCR reader to extract text, uses the Ollama client to process the text, masks the image with the parsed data, and returns the extracted data and masked image to the client.
*   `ollamaClient.py`: This file defines the `OllamaClient` class, which is responsible for interacting with the Ollama API. It initializes a client and has a method `askOllama` that sends a prompt to the Ollama model to extract PII from the Aadhaar card data.
*   `parser.py`: This file defines the `ocrReader` class, which uses the `easyocr` library to extract text from images and PDFs. The `readTextfromImage` method reads text from an image file, and the `readTextfromPdf` method converts a PDF file to an image and then reads text from the image.

## Setup Instructions

*   Install dependencies for the client: `cd client && npm install`
*   Install dependencies for the server:
    *   Instal required packages using the `server/requirements.txt` file

        ```
        fastapi
        uvicorn
        python-multipart
        easyocr
        pymupdf
        pdf2image
        Pillow
        ollama
        ```
    *   Install the dependencies: `cd server && pip install -r requirements.txt`
*   Set up the Ollama model.
*   Run the client: `cd client && npm run dev`
*   Run the server: `cd server && uvicorn main:app --reload`

## How to Use

*   Upload an Aadhaar card image or PDF through the client application.
*   The application will process the file and display the extracted PII and masked image.
