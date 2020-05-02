import requests

class RequestManager:

    def post(self, url, bytes_image, path):
        body = {
            'account':'alerodriguezangulo@gmail.com',
            'capture': bytes_image,
            'date': path.split('/')[2][:-4],
            'producer': 'door camera',
            'secret': 'somesecret'
        }
        response = requests.post(url, json = body)
        print(' [x] Request respose', response.status_code)