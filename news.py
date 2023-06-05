import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    for tr in soup.select("#wrap > table > tbody > tr"):
        title = tr.select_one("#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a")
        print(title.text.strip())