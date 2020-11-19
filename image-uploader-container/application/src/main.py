import os
import asyncio
import concurrent.futures

from consumer import Consumer


async def main():
    consumer = Consumer(mq_host, mq_queue, url)
    loop = asyncio.get_running_loop()

    await loop.run_in_executor(None, consumer.consume)


if __name__ == "__main__":
    mq_host = os.environ.get('MQ_HOST')
    mq_queue = os.environ.get('MQ_QUEUE')
    url = os.environ.get('ARGUS_UPLOAD_URL')
    captures_folder = os.environ.get('CAPTURES_FOLDER')

    asyncio.run(main())