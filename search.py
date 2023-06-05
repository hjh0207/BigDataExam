import requests
from bs4 import BeautifulSoup

def get_search():
    url = "https://signal.bz/"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        oo = soup.select_one('#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > a > span.rank-text')
        print(oo)
    else:
        print(f"HTTP 요청 실패 코드: {response.status_code}")