import time
from app.trader import run

while True:
    run()
    time.sleep(60)