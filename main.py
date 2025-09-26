import asyncio, random, time
from telethon import TelegramClient
from telethon.errors import FloodWaitError, RPCError

# --------------------------
# SENSİTİF BİLGİLER (SENİN VERDİKLERİN)
API_ID = 27065413
API_HASH = "fd0bec61df8c985830f2aaf804afff99"
phone = "+905448566871"
# hedef (senin verdiğin kullanıcı/kanal)
target = 'trarayisiniz'
# --------------------------

client = TelegramClient('session', API_ID, API_HASH)

async def main():
    # ilk olarak oturum aç (ilk çalıştırmada kod ister)
    await client.start(phone=phone)

    counter = 0
    while True:
        try:
            await client.send_message(target, 'Show için müsaitimmmm ❤️‍🔥')
            counter += 1

            if counter % 3 == 0:          # her 3 mesajda bir
                await asyncio.sleep(20)   # 20 sn bekle
            else:
                await asyncio.sleep(10)   # normalde 10 sn

        except FloodWaitError as fw:
            wait = int(getattr(fw, 'seconds', 60))
            print(f"[FloodWait] {wait}s bekleniyor — {time.ctime()}")
            await asyncio.sleep(wait + 5)
            counter = 0

        except RPCError as e:
            print(f"[RPCError] {e}. 60s bekleniyor — {time.ctime()}")
            await asyncio.sleep(60)
            counter = 0

        except Exception as e:
            print(f"[Hata] {e}. 60s bekleniyor — {time.ctime()}")
            await asyncio.sleep(60)
            counter = 0

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
