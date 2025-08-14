import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler

# Get environment variables
TOKEN = os.getenv("8347862417:AAENRuD173FzCvXBbXLgjnRnw6fRJ5VUTU8")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH, "/webhook")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Full URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Basic start command
@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Hello! Your Render Telegram bot is working ✅")

# Aiohttp app
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL + WEBHOOK_PATH)

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()

app = web.Application()
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == "__main__":
    web.run_app(app, port=int(os.getenv("PORT", 8080)))
