import os
import pyodbc
from time import sleep
from .chatbot import ChatBot

class AIAnnouncementManager:
    def __init__(self):
        API_KEY = os.getenv("api_key")
        self.GigaChat = ChatBot(API_KEY)
        self.interval = 5  # seconds

        DRIVER = os.getenv("DRIVER")
        SERVER = os.getenv("SERVER")
        UID = os.getenv("UID")
        PWD = os.getenv("PWD")
        Timeout = os.getenv("Timeout")
        self.connection_string = (
            f"DRIVER={DRIVER};"
            f"SERVER={SERVER};"
            f"UID={UID};"
            f"PWD={PWD};"
            f"Timeout={Timeout};"
        )

        self.conn = None
        for _ in range(1800):
            try:
                self.conn = pyodbc.connect(self.connection_string)
                print("Successful Connection!")
                break
            except Exception as e:
                print("Connection Denied\n\n\n", e)
                sleep(1)

    def sanitize_message(self, message: str, max_length: int = 90) -> str:
        # Tek tırnakları SQL güvenli karakterle değiştir
        message = message.replace("'", "’")  # Alternatif: message.replace("'", "''")
        
        # Özel karakterleri isteğe bağlı temizle (gerekmiyorsa bu kısmı çıkarabilirsin)
        message = ''.join(c for c in message if c.isprintable())

        # Mesajı kes (maksimum uzunluk sınırı)
        if len(message) > max_length:
            message = message[:max_length - 3] + "..."  # Fazlaysa sonuna "..." koy

        return message
    def get_announcements(self):
        query = """
        SELECT ID, _message FROM Panel_Silvarya.dbo._Announcement_AI
        WHERE Processed = 0
        ORDER BY ID ASC
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            msg = {"ID": row.ID, "_message": row._message}
            self.send_announcement(msg)

    def send_announcement(self, msg):
        msg_id = msg["ID"]
        msg_content = msg["_message"]
        ai_response = self.GigaChat.get_response(msg_content)
        ai_response = self.sanitize_message(ai_response)
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                EXEC Panel_Silvarya.dbo._SendMessage_FromAI @from_message_id = ?, @msg = ?
            """, msg_id, ai_response)

            # İşlendiyse işaretle
            cursor.execute("""
                UPDATE Panel_Silvarya.dbo._Announcement_AI
                SET Processed = 1 WHERE ID = ?
            """, msg_id)

            self.conn.commit()
            print(f"[✓] Sent: {msg_id} - {msg_content} as \t {ai_response}")
        except Exception as e:
            print(f"[X] Error sending message ID {msg_id}:", e)

