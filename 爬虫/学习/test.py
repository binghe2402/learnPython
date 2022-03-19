import requests
# import json


body = {
    "appToken": "AT_oistnMhv3L1lvyCBGX8vY6Desoy5jj9O",
    "content": "Wxpusher祝你中秋节快乐!",
    "summary": "消息摘要",
    "contentType": 1,
    "uids": [
        "UID_nHtjSh0L5w5PJw9OiTXDUH5Tvwlj"
    ],
    "url": "http://wxpusher.zjiecode.com"
}

r = requests.post(
    'http://wxpusher.zjiecode.com/api/send/message', json=body)

print(r)

http: // www.bili202.com/plugin.php?id = k_misign: sign & operation = qiandao & formhash = 3da3c5e0 & format = empty
