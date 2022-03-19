import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import os

import time
time.sleep(1)

path = ".\\attendance_log\\b02_log.txt"
if not os.path.exists(path):
    os.makedirs(path)
logging.basicConfig(
    filename=path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("start")
cookie = r"VEcf_2132_saltkey=P8tntDS7; VEcf_2132_lastvisit=1638889669; VEcf_2132_sid=F88Ae4; VEcf_2132_sendmail=1; UM_distinctid=17d95a6cf1784b-0113d3bd09c233-59191459-144000-17d95a6cf18678; CNZZDATA1278242140=98740942-1638890165-|1638890165; Hm_lvt_ee5e123f350a956a5f30523667238319=1638893279; VEcf_2132_seccodecSAhdjF88Ae4=8191.43289c08af47866074; VEcf_2132_ulastactivity=2562iFP/A417OmZg0gCPU1q1BAMJXcjKJp4+XmyiWAdz8/pEW2KL; VEcf_2132_auth=0ac9iHgqwd8eRJCOdp04azHLYCV4g8iIsImSB002xkuFaK4KdmwDaBzkgKUk3EKrJO755ob0K3UavS1AQtR/8adzFsU; VEcf_2132_lastcheckfeed=737044|1638893349; VEcf_2132_lip=139.162.192.70,1638892135; Hm_lpvt_ee5e123f350a956a5f30523667238319=1638893353; VEcf_2132_lastact=1638893355	misc.php	patch"
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
    'http': 'http://127.0.0.1:7890',
    'https': 'https://127.0.0.1:7890',
}

url = 'http://www.bili202.com/k_misign-sign.html'

res = s.get(url, proxies=proxies)

soup = BeautifulSoup(res.text)
pars = {}
for each in soup.find(id="JD_sign").get('href').split('?')[1].split('&'):
    key, val = each.split('=')
    pars[key] = val

logging.info(pars)

attendence_url = 'http://www.bili202.com/plugin.php'

r = s.get(attendence_url, params=pars, proxies=proxies)
print(r.text)
print("\n")

s.close()

if 'xml' in r.text:

    body = {
        "appToken": "AT_oistnMhv3L1lvyCBGX8vY6Desoy5jj9O",
        "content": "b02签到成功",
        "summary": "b02签到成功",
        "contentType": 1,
        "uids": [
            "UID_nHtjSh0L5w5PJw9OiTXDUH5Tvwlj"
        ],
        "url": "http://www.bili202.com/k_misign-sign.html"  # 原文链接，可选参数
    }

    r = requests.post(
        'http://wxpusher.zjiecode.com/api/send/message', json=body)
    print(r.text)
