import os
import time
from random import randint

import requests
from bs4 import BeautifulSoup

query_id = ["mproPpoq6O", "KqndgxeLl9", "WnBe01o371", "wWmoO5Rd4E", "Jb0vmloB1G",
            "74KvxwokxM", "KMZd7VOvrO", "Q1Vd5Ko85R", "DpQvNABoNE", "Y2KeDGQdNP",
            "NKGoRAzel6", "mDOvnyBoEB", "5VaobgvAj1", "x9ozB4KoXb", "7Gdab3peQy",
            "74Kvx59dkx", "NRrvWq3e5z", "qENeYpdY49", "x9ozqX7eXb", "x9ozBY7oXb",
            "rx9ozj7oXb", "KqndgDmeLl", "KMZd7X3erO", "Jb0vml8oB1", "YqoXQEqvOD",
            "KMZd76vrOw", "wWmoOVYe4E", "YqoXQR0vOD", "n3moBE1eN5", "LBwdG0jePx",
            "DgeyrgMoZq", "5VaobmGeAj", "nBe0WR5d37", "Q0or4Wnd8B", "YqoXQGXvOD",
            "qYwv4MNdPa", "NRrvWG1v5z", "Kqndg1xoLl", "rYqoXQ8vOD", "20MdKx4ew1",
            "6ARe1YLe7n", "Om4ej8mvxE", "b0vmYyJvB1", "VaobmGneAj", "rYqoXz6dOD"]
query_name = ["知乎 ‧ 热榜", "微博 ‧ 热搜榜", "微信 ‧ 24h热文榜", "澎湃 ‧ 热榜", "百度 ‧ 实时热点",
              "哔哩哔哩 ‧ 全站日榜", "知乎日报 ‧ Today", "36氪 ‧ 24小时热榜", "抖音 ‧ 热门视频榜", "少数派 ‧ 热门文章",
              "吾爱破解 ‧ 今日热帖", "豆瓣电影 ‧ 豆瓣新片榜", "虎嗅网 ‧ 热文", "今日头条 ‧ 头条热榜", "淘宝 ‧ 天猫 ‧ 每日爆款清单",
              "IT之家 ‧ 日榜", "煎蛋 ‧ 一周热文", "AcFun ‧ 排行榜", "今日热卖 ‧ 全网线报聚合", "财新网 ‧ 点击排行榜",
              "新浪财经新闻 ‧ 点击量排行", "开眼视频 ‧ 日报", "历史上的今天 ‧ Today", "宽带山 ‧ 24小时热帖", "高楼迷 ‧ 今日热帖",
              "过早客（光谷社区） ‧ 今日热议", "机核网 ‧ 每日最新", "3DM游戏网 ‧ 最新新闻", "懂球帝 ‧ 今日头条", "Product Hunt ‧ 今日新产品",
              "CSDN博客 ‧ 综合热榜", "开发者头条 ‧ 今日头条", "Dribbble ‧ 实时流行", "优设网 ‧ 每日热文榜单", "汽车之家 ‧ 论坛精选日报",
              "安全客 ‧ 最新", "安全脉搏 ‧ 最新", "看雪论坛 ‧ 最新精华", "GitHub ‧ Trending Today", "人人都是产品经理 ‧ 日榜",
              "虎扑社区 ‧ NBA论坛热帖", "游研社 ‧ 首页推荐", "纵横中文网 ‧ 24小时畅销榜", "起点中文网 ‧ 24小时热销榜", "厦门小鱼 ‧ 今日热帖"]

headers = {'Content-Type': "application/x-www-form-urlencoded",
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
           }

def tophubToday()-> list:
    searchTerms = []
    saveList = []
    search_terms = []
    for x in range(len(query_id)):
        print(f"query_name_{x} 为：", str(query_name[x]))
        r = requests.get(f"https://tophub.today/n/{query_id[x]}", headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        tdList = soup.find_all('td',attrs={"class": "al"})
        for td in tdList:
            searchTerms.append(td.get_text())
        time.sleep(randint(8, 10))
    searchTerms = list(set(searchTerms))
    
    if not os.path.exists("./totalWords.txt") :
        search_terms = readFile("./words.txt")
        tempList = list(set(searchTerms) - set(search_terms))
        saveList = [item.replace('\n', '').replace('\r', '').replace("?", "").replace("/", " ") for item in tempList if len(item) > 2]
        search_terms.extend(saveList)
        saveFile(saveList, "./totalWords.txt")
    else:
        search_terms = readFile("./totalWords.txt")
        tempList = list(set(searchTerms) - set(search_terms))
        saveList = [item.replace('\n', '').replace('\r', '').replace("?", "").replace("/", " ") for item in tempList if len(item) > 2]
        search_terms.extend(saveList)
        saveFile(saveList, "./totalWords.txt")
    print(f"search_terms 长度：{len(search_terms)}")
    print(f"saveList 长度：{len(saveList)}")
    return list(filter(None,saveList))

def saveFile(data: list, file_name: str):
    if len(readFile(file_name)) > 15000:
        with open(file_name,"w",encoding="utf-8") as f:
            f.write("\n".join(data))
            f.write("\n")
    else:
        with open(file_name,"a",encoding="utf-8") as f:
            f.write("\n".join(data))
            f.write("\n")


def readFile(file_name: str) -> list:
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return eval(f.read())
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().splitlines()

if __name__ == "__main__":
    saveList = tophubToday()
    oldWords = readFile("./words.txt")
    saveFile(saveList, "./words.txt")
    oldWords.extend(saveList)
    print(len(oldWords))
