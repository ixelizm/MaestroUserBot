from pyrogram import Client
from logging import CRITICAL, DEBUG, INFO, basicConfig, getLogger

app = Client(
  "Maestro",
  1038911,
  "94d21cd31f1d54ff715ead95b1777bc1",
  plugins = dict(root="bot/plugins")
)

logger = getLogger(__name__)
basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=INFO,
)
