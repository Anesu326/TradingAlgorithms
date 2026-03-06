from fastapi import FastAPI
from app.state import bot_state

app = FastAPI()

@app.get("/status")
def status():
    return bot_state

@app.post("/start")
def start_bot():
    bot_state["running"] = True
    return {"message": "bot started"}

@app.post("/stop")
def stop_bot():
    bot_state["running"] = False
    return {"message": "bot stopped"}

