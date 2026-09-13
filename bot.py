import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from telegram import Bot

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

TIMEZONE = ZoneInfo("Asia/Singapore")

REMINDER_TIMES = {
    "09:00",
    "11:00",
    "13:00",
    "15:00",
    "17:00",
    "19:00",
    "21:00",
}

bot = Bot(token=BOT_TOKEN)


async def send_water_reminder():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="💧 Water break! Have a glass of water."
    )


async def main():
    print("Water reminder bot started.")

    last_reminder = None

    while True:
        now = datetime.now(TIMEZONE)

        current_time = now.strftime("%H:%M")
        today = now.strftime("%Y-%m-%d")

        reminder_key = f"{today}-{current_time}"

        if current_time in REMINDER_TIMES:
            if reminder_key != last_reminder:
                print(f"Sending reminder at {current_time}")

                try:
                    await send_water_reminder()
                    last_reminder = reminder_key

                except Exception as e:
                    print(f"Telegram error: {e}")

        await asyncio.sleep(20)


if __name__ == "__main__":
    asyncio.run(main())
