import requests, sys

S = int(input("请输入期数："))
SS = 213 + 2 * (S - 20)

try:
    with open("花名册.txt", encoding='utf-8') as f:
        names = [i.strip() for i in f.readlines()]
    with open("信息.txt", encoding='utf-8') as f:
        lv = f.readlines()
    
except:
    with open("花名册.txt") as f:
        names = [i.strip() for i in f.readlines()]   
    with open("信息.txt") as f:
        lv = f.readlines()

url = f"http://dxx.ahyouth.org.cn/api/peopleRankStage?table_name=reason_stage{SS}&level1={lv[0]}&level2={lv[1]}&level3={lv[2]}&level4={lv[3]}"
print(lv[3], "\n")

headers = {"Accept": "*/*", 
           "Accept-Encoding": "gzip, deflate", 
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 
           "Connection": "keep-alive",
           "Host": "dxx.ahyouth.org.cn",
           "Referer": "http://dxx.ahyouth.org.cn/",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"}

try:
    r = requests.get(url=url, headers=headers)
except:
    print("网络错误")
    input()
    sys.exit()
temp = r.json()['list']['list']
done = [n['username'] for n in temp]

for i in done:
    try:
        names.remove(i)
    except(ValueError):
        print(f"发现一个不在花名册中的完成成员：{i}")
        
print(f"共有{len(names)}名同学未完成")
for i, n in enumerate(names):
    print(f"{i+1}：{n}")
input()
