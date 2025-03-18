from dotenv import load_dotenv
from time import sleep
from src.client import Client
import os
import asyncio
import json
load_dotenv('.env')

class Runner():
    async def main(self):
        client = Client()
        self.handle_channels()
        await client.login(os.getenv('TIESKEY_TOKEN'))
        await client.connect()

    def handle_channels(self):
        self.config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        try:
            with open(self.config_path, "r") as file:
                config = json.load(file)

            target_value = 1335718415465316393
            for key, value in config.items():
                if value == 0:
                    config[key] = target_value
                sleep(5)

            with open(self.config_path, "w") as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            print(f"An error occurred while processing the config file: {str(e)}")

if __name__ == "__main__":
    runner = Runner()
    asyncio.run(runner.main())
