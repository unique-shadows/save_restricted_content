from flask import Flask, redirect
import os

bot_name = os.getenv("BOT_NAME")
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(f"https://t.me/{bot_name}")