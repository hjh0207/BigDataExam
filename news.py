import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"

# HTTP GET 요청을 보냅니다.
response = requests.get(url)

# 응답 데이터의 인코딩을 확인하고, 필요에 따라 설정합니다.
response.encoding = "utf-8"

# 응답 데이터를 파싱합니다.
soup = BeautifulSoup(response.text, "html.parser")

# 속보 기사 제목을 찾습니다.
titles = soup.select(".hdline_cluster_more .cluster_text > a")

# 결과를 출력합니다.
for title in titles:
    print(title.text.strip())
