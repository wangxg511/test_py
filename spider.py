import requests

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

url = 'http://sz.ozguard.cn/app/index.php?i=1&c=entry&type=uids&id=4921&hdid=80&do=list&m=w01_vote&wxdm=1&wxref=mp.weixin.qq.com'
session = requests.Session()
rep = session.post(url,
                   headers=header)
# print(rep.content.decode("utf8"))
# print(rep.request.headers)
toupiao_url = 'http://sz.ozguard.cn/app/index.php?i=1&c=entry&id=4921&hdid=80&do=Cgong&m=w01_vote'
rep = session.get(toupiao_url,headers=header)
print(rep.content.decode("utf8"))
