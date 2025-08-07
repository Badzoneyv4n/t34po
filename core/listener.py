import os
import re
from datetime import datetime
from telethon import events, TelegramClient
from dotenv import load_dotenv
from utils.tracker import update_balance, report_hourly

load_dotenv()

API_ID = int(os.getenv("Tel_API_ID")) # type: ignore
API_HASH = os.getenv("Tel_API_HASH")
SESSION_NAME = "t34_session"
BOT_USERNAME = "PocketSignalBot"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH) # type: ignore

@client.on(events.NewMessage(from_users=BOT_USERNAME))
async def po_signal_listener(event):
    text = event.message.text or ""

    # Accept signal button
    if 'SIGNAL' in text and event.buttons:
        try:
            for i, row in enumerate(event.buttons):
                for j, button in enumerate(row):
                    if 'Accept' in button.text:
                        await event.click(i, j)
                        print("✅ Signal accepted.")
                        return
        except Exception as e:
            print(f"❌ Failed to click Accept: {e}")

    # Balance message
    match = re.search(r"Your current balance: \$([0-9.]+)", text)
    if match:
        balance = float(match.group(1))
        update_balance(balance)
        report_hourly()

async def start_bot():
    print("🚀 T34Po running... waiting for PocketOption signals.")
    await client.start() # type: ignore
    await client.run_until_disconnected() # type: ignore
