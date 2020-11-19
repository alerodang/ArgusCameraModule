import requests
import os
import json

class RequestManager:

    def post(self, url, bytes_image, path, timeout):
        body = {
            'account': os.environ.get('ACCOUNT'),
            'capture': bytes_image,
            'date': path.split('/')[2][:-4],
            'producer': os.environ.get('PRODUCER_NAME'),
            'secret': os.environ.get('PRODUCER_SECRET')
        }
        response = requests.post(url, data=json.dumps(body), timeout=timeout)
        print(' [x] Request respose', response.status_code)