import requests
import re
import base64
from urllib.parse import quote


q = input("请输入fofa命令: ")
k = quote(f'{q}', 'utf-8')
w = q.encode("utf-8")

qbase64 = base64.b64encode(w)
qbase64 = qbase64.decode('utf-8')

sum = 3
headers = {
    'Host': 'api.fofa.info',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://fofa.info/',
    #   这里的Authorization换用你自己的,获取方式视频演示见b站ID:das_Lighting
    'Authorization': '这里填写你的Authorization',
    'Origin': 'https://fofa.info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Te': 'trailers',
    'Connection': 'close',
}

url = f"https://api.fofa.info/v1/search?q={k}&qbase64={qbase64}&full=false&pn=1&ps=20"
total_sum1 = requests.get(url=url,headers=headers)

fofa_sum = re.compile(r'"total":(?P<total_sum>.*?)}}}', re.S)

result_sum = fofa_sum.finditer(total_sum1.text)

for j in result_sum:
    total = j.group('total_sum')
    total = int(total)

    sum = total // 20 + 2

    print("总共有" , total, "条数据," , sum-1, "列")
with open(r'urls.txt',mode='at',encoding='utf-8') as f:
    for time in range(1,sum):
        url = f"https://api.fofa.info/v1/search?q={k}&qbase64={qbase64}&full=false&pn={time}&ps=20"


        a = requests.get(url=url,headers=headers)


        fofa = re.compile(r'"host":"(?P<name>.*?)","icp":', re.S)

        result = fofa.finditer(a.text)

        for i in result:

            a = i.group('name')
            if len(a) < 50:

                f.writelines(a + '\n')

        if (time - 1) % 5 == 0:
            print("第", (time - 1)//5, "页已经爬完!")



print("爬取完毕!")

