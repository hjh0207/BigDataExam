import database
import dmovie
import geni
import news

print('실시간 트렌드 보기')
print('1.데이터 갱신')
print('2.실시간 검색어 보기')
print('3.실시간 뉴스속보 보기')
print('4.일간 노래순위 보기')
print('5.영화 예매순위 보기')


# 사용자에게 입력받기
num = input('선택 번호 입력: ')

# 만약에 1번이면 멜론 정보 가져와서 디비에 저장
if num == '1':
    print('정보 가져와서 디비에 저장')
# 만약에 2번이면 디비에 저장된 데이터 보기
elif num == '2':
    print('디비에 저장된 데이터 보기')
    inssa = database.get_data() # 디비에서 데이터 가져오기
    for m in inssa:
        print(f"{m[0]}위 {m[1]} - {m[2]}")