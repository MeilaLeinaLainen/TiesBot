from dotenv import load_dotenv
load_dotenv('.env')

import os, asyncio
from src.client import Client

class Runner():
    async def main():
        client = Client()
        await client.login(os.getenv('TIESKEY_TOKEN'))
        await client.connect()

asyncio.run(Runner.main())