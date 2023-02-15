import json

import requests as rq

path = "/hust/labor"
port = "5701"


def send_labor_list(data):
    send_data = json.dumps(data)
    rq.post("http://127.0.0.1:{0}/{1}".format(port, path), data=send_data)
