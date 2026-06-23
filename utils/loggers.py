import logging 
import os

os.makedirs("logs",exist_ok=True)



logging.basicConfig(filename="logs/app.log",
                    format="%(asctime)s  [% (level)s] %(message)s" ,
                    level= logging.DEBUG
                    )

logger = logging.getLogger(__name__)