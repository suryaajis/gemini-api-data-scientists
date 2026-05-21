import os
import base64
import urllib.request
import httpx
import PIL.Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Create a .env file with: GEMINI_API_KEY=your_key_here")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


# ============================================================
# 1. TEXT GENERATION
# ============================================================
def text_generation():
    response = model.generate_content("Explain how AI works")
    print(response.text)


# ============================================================
# 2. STREAMING RESPONSE
# ============================================================
def streaming_response():
    response = model.generate_content("Explain how AI works", stream=True)
    for chunk in response:
        print(chunk.text, end="")
    print()


# ============================================================
# 3. LIST AVAILABLE MODELS
# ============================================================
def list_models():
    for m in genai.list_models():
        print(m.name)


# ============================================================
# 4. IMAGE INPUT
# ============================================================
def image_input():
    image_url = "https://marketplace.canva.com/EAFhLHB9S8g/1/0/900w/canva-pink-putih-minimalist-salon-price-list-28N6AZMRZKI.jpg"
    urllib.request.urlretrieve(image_url, "salon_price_list.jpg")

    img = PIL.Image.open("salon_price_list.jpg")

    response = model.generate_content(["", img])
    print("-- Without prompt --")
    print(response.text)

    response = model.generate_content(["buatlah table dari response tersebut", img])
    print("\n-- With table prompt --")
    print(response.text)

    prompt = """buatlah tabel dari response tersebut,
buatlah code python untuk membuat dataframe dari tabel tersebut"""
    response = model.generate_content([prompt, img])
    print("\n-- With DataFrame prompt --")
    print(response.text)


# ============================================================
# 5. DOCUMENT UNDERSTANDING (PDF)
# ============================================================
def document_understanding():
    doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    doc_data = base64.standard_b64encode(httpx.get(doc_url).content).decode("utf-8")
    response = model.generate_content([{"mime_type": "application/pdf", "data": doc_data}, "Summarize this document"])
    print(response.text)


# ============================================================
# 6. AUDIO UNDERSTANDING
# ============================================================
def audio_understanding():
    audio_url = "https://storage.googleapis.com/generativeai-downloads/data/State_of_the_Union_Address_30_January_1961.mp3"
    urllib.request.urlretrieve(audio_url, "sample.mp3")

    myfile = genai.upload_file("sample.mp3")
    result = model.generate_content([myfile, "Describe this audio clip"])
    print(result.text)


# ============================================================
# 7. CHAT CONVERSATION
# ============================================================
def chat_conversation():
    chat = model.start_chat(history=[])

    response = chat.send_message("Dalam satu kalimat, jelaskan cara kerja komputer kepada anak kecil.")
    print(f"[USER] Dalam satu kalimat, jelaskan cara kerja komputer kepada anak kecil.")
    print(f"[MODEL] {response.text}")

    response = chat.send_message("Jelaskan cara membuat otomatisasi email")
    print(f"\n[USER] Jelaskan cara membuat otomatisasi email")
    print(f"[MODEL] {response.text}")


def chat_with_history():
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    response = chat.send_message("I have 2 dogs in my house.")
    print(f"[USER] I have 2 dogs in my house.")
    print(f"[MODEL] {response.text}")

    response2 = chat.send_message("How many paws are in my house?")
    print(f"[USER] How many paws are in my house?")
    print(f"[MODEL] {response2.text}")


# ============================================================
# JALANKAN FUNCTION YANG DIINGINKAN DI SINI
# Uncomment baris yang ingin dijalankan, comment sisanya
# ============================================================
if __name__ == "__main__":
    text_generation()
    # streaming_response()
    # list_models()
    # image_input()
    # document_understanding()
    # audio_understanding()
    # chat_conversation()
    # chat_with_history()
