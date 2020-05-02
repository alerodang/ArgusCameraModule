import pika
import json

from image_uploader_service import ImageUploaderService

class Consumer:
    
    def __init__(self, mq_host, queue, url):
        self.mq_host = mq_host
        self.queue = queue
        self.image_uploader_service = ImageUploaderService(url)

    def callback(self, ch, method, properties, body):
        json_body = json.loads(body.decode('utf-8'))
        path = json_body.get('path')
        print(' [x] Loading image from', path)
        image = self.image_uploader_service.get_image(path)
        print(' [x] Send image')
        self.image_uploader_service.send_image(image, path)

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.mq_host))

        channel = connection.channel()

        channel.queue_declare(queue=self.queue)

        channel.basic_consume(queue=self.queue,
                        auto_ack=True,
                        on_message_callback=self.callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()