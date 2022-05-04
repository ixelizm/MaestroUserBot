from bot import app, logger
from pyrogram import idle

if __name__ == "__main__":
  app.start()
  logger.info("Bot başlatıldı!")
  idle()


