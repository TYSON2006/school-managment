import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("school")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/app.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)





















