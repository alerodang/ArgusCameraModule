import requests

from request_manager import RequestManager


class ImageUploaderService:
    
    def __init__(self, url):
        self.url = url
        self.request_manager = RequestManager()

    def send_image(self, image):
        request_manager.post(self.url, image)
        
    def getImage(path):
        return '' # TODO

print(x.text)