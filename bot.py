from telegram import Update
from telegram.ext import Application, CommandHandler
import logging
from datetime import datetime

# Enable logging for debugging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define start command
async def start(update: Update, context):
    await update.message.reply_text("Hello! Send /today to get today's lessons.")

# Define lesson schedule
lesson_schedule = {
    "Monday": "15.00-16.20 | Бакалавр 2 курс, ГМ 205/206 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari asoslari (ma'руза)\nA. Pulatov, 11-110",
    "Tuesday": "10.00-11.20 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari asoslari (ma'руза)\nA. Pulatov, 11-110\n\n"
                "15.00-16.20 | Бакалавр 2 курс, ГМ 206 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari asoslari (амалийот)\nS. Xamidjonov, 11-110",
    "Wednesday": "No lesson",
    "Thursday": "8.30-9.50 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari asoslari (амалий)\nB. Mamadaliyev, 11-406\n\n"
                 "10.00-11.20 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari асослари (амалий)\nB. Mamadaliyev, 11-406",
    "Friday": "8.30-9.50 | Бакалавр 1 курс, АТ 119 гуруҳ, (ўзбек тилида) | Atrof-muhit fanlari (амалийот)\nB. Mamadaliyev, 11-406\n\n"
              "8.30-9.50 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | CAD/CAM/CAE tizimida loyihalash (амалийот)\nS. Xamidjonov, 11-110\n\n"
              "10.00-11.20 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | CAD/CAM/CAE tizimida loyihalash (амалийот)\nS. Xamidjonov, 11-110\n\n"
              "16.30-17.50 | Бакалавр 2 курс, ГМ 205 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari асослари (амалий)\nB. Mamadaliyev, 11-406",
    "Saturday": "8.30-9.50 | Бакалавр 2 курс, АТБР 216 гуруҳ, (ўзбек тилида) | CAD/CAM/CAE tizimida loyihalash (ма'руза)\nA. Pulatov, 11-110\n\n"
                "11.30-12.50 | Бакалавр 2 курс, ГМ 205 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari асослари (амалий)\nB. Mamadaliyev, 11-406\n\n"
                "13.30-15.00 | Бакалавр 2 курс, ГМ 206 гуруҳ, (ўзбек тилида) | Geoaxborot tizimlari асослари (амалийот)\nS. Xamidjonov, 11-110",
    "Sunday": "No lesson",
}

# Define /today command
async def today(update: Update, context):
    day = datetime.today().strftime("%A")  # Get current day
    lessons = lesson_schedule.get(day, "No lessons today.")
    await update.message.reply_text(f"📅 *{day}* Lessons:\n\n{lessons}")

# Main function to run the bot
def main():
    TOKEN = "7583601663:AAHla4GUt0TUpKNaycSXUbRnTx9A8k0SWPM"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("today", today))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
import os

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))  # Get port from Render
    main()