import asyncio, random
from telethon import TelegramClient

API_ID=27065413
API_HASH="fd0bec61df8c985830f2aaf804afff99"
phone = "+905448566871"

client = TelegramClient('session', api_id, api_hash)

async def main():
    counter = 0
    while True:
        try:
            await client.send_message('trarayisiniz',
                                      'Show için müsaitimmmm ❤️‍🔥')
            counter += 1
            if counter % 3 == 0:          # her 3 mesajda bir
                await asyncio.sleep(20)   # 20 sn bekle
            else:
                await asyncio.sleep(10)   # normalde 10 sn
        except Exception as e:
            print("Hata:", e)
            await asyncio.sleep(60)       # 1 dk bekle
            counter = 0                    # sayaç sıfırla
