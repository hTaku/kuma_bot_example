import requests

class Line(object):
    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def post_notify(self, 
                    message,
                    image=None,
                    sticker_package_id=None,
                    sticker_id=None,):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
        }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        requests.post(
            Line.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
        )