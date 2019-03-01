import json

import requests


class YunPain(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "您的验证码是{code}".format(code=code),
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pain = YunPain("ab45b3863e40a0dcf70b731fb93e1ab1")
    yun_pain.send_sms("555", "13427498660")
