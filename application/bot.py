import requests

from main_app import settings

TELEGRAM_API = "https://api.telegram.org/"
BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
BOT_SLUG = f"bot{BOT_TOKEN}/"
CHAT_ID = "-926016123"


class TelegramBot:
    CONTACT = TELEGRAM_API + BOT_SLUG

    @classmethod
    def send_message(cls, message):
        function = "sendMessage"
        url = cls.CONTACT + function

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        print(requests.get(url, params=payload))


if __name__ == "__main__":
    print(TelegramBot.CONTACT)
    TelegramBot.send_message("Test massage")
