import base64

from request_manager import RequestManager


class ImageUploaderService:
    
    def __init__(self, url):
        self.url = url
        self.request_manager = RequestManager()

    def send_image(self, image, path):
        self.request_manager.post(self.url, image, path, 1)
        
    def get_image(self, path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')