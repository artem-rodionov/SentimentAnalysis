import logging
from services.MLService import run
import asyncio

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("grpc").setLevel(logging.INFO)

    asyncio.run(run())