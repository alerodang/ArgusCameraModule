import os

from consumer import Consumer


if __name__ == "__main__":
    mq_host = os.environ.get('MQ_HOST')
    mq_queue = os.environ.get('MQ_QUEUE')
    url = os.environ.get('ARGUS_UPLOAD_URL')
    captures_folder = os.environ.get('CAPTURES_FOLDER')

    consumer = Consumer(mq_host, mq_queue, url)

    consumer.consume()
