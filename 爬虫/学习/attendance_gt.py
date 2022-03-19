import requests
from bs4 import BeautifulSoup
# from datetime import datetime
# import logging
# import os

# import time
# time.sleep(1)

# path = ".\\attendance_log\\b02_log.txt"
# if not os.path.exists(path):
#     os.makedirs(path)
# logging.basicConfig(
#     filename=path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# logging.info("start")
cookie = r"uLXw_2132_saltkey=NW87xbOU; uLXw_2132_lastvisit=1639755570; uLXw_2132_seccodecS=22514.b1e47e4dc6a89c58e4; uLXw_2132_auth=4098SSKO8mcNI9E1Ic6v0oK%2Bb0I%2BfpuXlp%2B7l9NxPZaAvApWsMDjgojzpoEZaVNuaiyQjrz4BDi5gVqj0qk8sM2MtB8; uLXw_2132_lastcheckfeed=731438%7C1639759228; uLXw_2132_lip=45.63.127.206%2C1639759228; uLXw_2132_nofavfid=1; uLXw_2132_atarget=1; uLXw_2132_home_diymode=1; uLXw_2132_smile=2D1; uLXw_2132_seccodecSAY920=4424.5b33000d21503023c2; uLXw_2132_seccodecSAcSP0=5907.22c3c4d883f95bb5ab; uLXw_2132_seccodecSAp9z0=6842.0229330ccd62e1a697; uLXw_2132_seccodecSASA10=10507.2ecffd6d82bcd6993a; uLXw_2132_seccodecSAOtU0=10621.dc344e2c2405dc4ad6; uLXw_2132_seccodecSAz110=10633.9ee518ed3a1ce35c9f; uLXw_2132_sid=0; uLXw_2132_visitedfid=41D84D88D49D37D2; uLXw_2132_st_p=731438%7C1641351415%7C77cea0c05fb254f03ee6e97d8fa98c7b; uLXw_2132_viewid=tid_265397; uLXw_2132_st_t=731438%7C1641351439%7C9c92a70d4ac917b85132f6ae066c7d46; uLXw_2132_forum_lastvisit=D_84_1641351065D_41_1641351439; uLXw_2132_onlineusernum=508; uLXw_2132_ulastactivity=1641454777%7C0; uLXw_2132_lastact=1641454779%09home.php%09misc; uLXw_2132_sendmail=1"
cookies = {}
for each in cookie.split(';'):
    key, val = each.strip().split('=', 1)
    cookies[key] = val

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}


filetype = "jpg"
s = requests.session()

s.cookies.update(cookies)
s.headers.update(header)

proxies = {
    'http': 'http://127.0.0.1:16000',
    'https': 'https://127.0.0.1:16000',
}

url = 'https://www.gtloli.gay/forum.php'

res = s.get(url, proxies=proxies)

soup = BeautifulSoup(res.text)
pars = {}
for each in soup.find(id="JD_sign").get('href').split('?')[1].split('&'):
    key, val = each.split('=')
    pars[key] = val

# logging.info(pars)

attendence_url = 'https://www.gtloli.gay/plugin.php'

r = s.get(attendence_url, params=pars, proxies=proxies)
print(r.text)
print("\n")

s.close()

if 'xml' in r.text:

    body = {
        "appToken": "AT_oistnMhv3L1lvyCBGX8vY6Desoy5jj9O",
        "content": "gt签到成功",
        "summary": "gt签到成功",
        "contentType": 1,
        "uids": [
            "UID_nHtjSh0L5w5PJw9OiTXDUH5Tvwlj"
        ],
        "url": "https://www.gtloli.gay/forum.php"  # 原文链接，可选参数
    }

    r = requests.post(
        'http://wxpusher.zjiecode.com/api/send/message', json=body)
    print(r.text)
