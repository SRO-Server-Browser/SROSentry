import os
import google.generativeai as genai


class ChatBot:
    NAME = "VSRO"  # Karakterimize bir isim verelim
    ROLE_PROMPT = f"Sen, Silkroad oyununda oyunculara rehberlik eden, esprili ve beklenmedik yorumlar yapan {NAME} adlı bir karaktersin. Cevapların maksimum 150 karakter olmalı. Oyun mekanikleri hakkında bilgi verirken dahi espri yapmaktan çekinme. Cevapların kısa, doğrudan ve komik olsun."

    def __init__(self, API_KEY):
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        self.chat = self.model.start_chat(history=[
            {
                "role": "user",
                "parts": [self.ROLE_PROMPT]
            },
            {
                "role": "model",
                "parts": ["Anlaşıldı! 150 karakteri aşmayacak şekilde esprili yanıtlar vermeye hazırım. Mesajları bekliyorum."]
            }
        ])

    def get_response(self, normal_message):
        prompt = f"İşte oyuncuya iletmem gereken mesaj: '{normal_message}'. Bu mesajı kısa, doğrudan ve beklenmedik bir espriyle oyuncuya aktar. Cevabın maksimum 150 karakter olsun."
        response = self.chat.send_message(prompt)
        return response.text.strip()[:150]  # Yanıtı 150 karakterle sınırla

if __name__ == "__main__":
    # API anahtarınızı ortam değişkeninden alın veya doğrudan buraya yazın
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY ortam değişkeni tanımlanmamış!")
    else:
        GigaChat = ChatBot(api_key)

        normal_mesaj1 = "Capture the flag event started"
        response1 = GigaChat.get_response(normal_mesaj1)
        print(f"Normal Mesaj: {normal_mesaj1}\n{GigaChat.NAME}: {response1}\n")

        normal_mesaj2 = "Serverimiz 1 saat sonra bakıma alınacaktır"
        response2 = GigaChat.get_response(normal_mesaj2)
        print(f"Normal Mesaj: {normal_mesaj2}\n{GigaChat.NAME}: {response2}\n")

        normal_mesaj3 = "Yeni bir oyuncu katıldı"
        response3 = GigaChat.get_response(normal_mesaj3)
        print(f"Normal Mesaj: {normal_mesaj3}\n{GigaChat.NAME}: {response3}")