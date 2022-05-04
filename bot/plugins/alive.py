from pyrogram import filters
from bot import app

@app.on_message(filters.regex(".alive") &filters.me)
async def aliveFunc(client, message):
  await message.edit("test")

