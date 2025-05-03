import dotenv
import time
from core.msg_handler import AIAnnouncementManager
import json  # JSON verilerini işlemek için

dotenv.load_dotenv()

AIAM = AIAnnouncementManager()
DEFAULT_SLEEP_TIME = 5
RETRY_SLEEP_TIME = 180

while True:
    response = AIAM.get_announcements()

    if response and isinstance(response, str) and "quota_dimensions" in response and "retry_delay" in response:
        try:
            error_data = json.loads(response)
            retry_seconds = 180  # Default olarak 3 dakika bekle
            for item in error_data:
                if "retry_delay" in item and "seconds" in item["retry_delay"]:
                    retry_seconds = item["retry_delay"]["seconds"]
                    break
            print(f"Kota aşımı tespit edildi. {retry_seconds} saniye bekleniyor...")
            time.sleep(retry_seconds)
        except json.JSONDecodeError:
            print("Kota aşımı hatası işlenirken JSON çözme hatası oluştu. Default süre bekleniyor.")
            time.sleep(RETRY_SLEEP_TIME)
    else:
        time.sleep(DEFAULT_SLEEP_TIME)