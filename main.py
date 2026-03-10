from pyrogram import Client
from datetime import datetime
import asyncio

api_id = 20138889
api_hash = "78f74c56390088f2afc04de6d7c3c88f"

app = Client("userbot", api_id=api_id, api_hash=api_hash)

async def update_clock():
    async with app:
        while True:
            now = datetime.now().strftime("%H:%M")
            await app.update_profile(bio=f"🕐 {now}")
            await asyncio.sleep(60)

asyncio.run(update_clock())
