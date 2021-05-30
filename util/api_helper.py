import json
from dataclasses import dataclass
from types import SimpleNamespace

import requests

from util.log_helper import getLogger

logger = getLogger()


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    obj: SimpleNamespace


class APIRequest:
    def post(self, url=None, payload=None, headers=None):
        print("sending post request with url:{} payload:{} headers:{}".format(url, payload, headers))
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def get(self, url=None, headers=None):
        print("sending get request with url:{} headers:{}".format(url, headers))
        response = requests.get(url, headers=headers)
        return self.__get_responses(response)

    def put(self, url=None, headers=None, payload=None):
        print("sending put request with url:{} payload:{} headers:{}".format(url, payload, headers))
        response = requests.put(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url=None, headers=None, payload=None):
        print("sending delete request with url:{} payload:{} headers:{}".format(url, payload, headers))
        response = requests.delete(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def __get_responses(self, response=None):
        status_code = response.status_code
        text = response.text
        obj = None
        if text != '':
            obj = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        try:
            as_dict = response.json()
        except Exception as err:
            print("Got exception message {}".format(str(err)))
            as_dict = {}
        headers = response.headers
        print("Got response values status code:{} response text:{} response json:{} response headers:{}".format(
            status_code, text, as_dict, headers))
        return Response(
            status_code, text, as_dict, headers, obj
        )