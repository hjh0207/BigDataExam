from database import drop_tb, create_tb, save_data, get_data
import dmovie
import geni
import news

print('실시간 트렌드 보기')
print('1.데이터 갱신')
print('2.실시간 검색어 보기')
print('3.실시간 뉴스속보 보기')
print('4.일간 노래순위 보기')
print('5.영화 예매순위 보기')

num = input('선택 번호 입력: ')

if num == '1':
    print('정보 가져와서 디비에 저장')
    drop_tb()
    create_tb()
    inssa = geni.genie()
    save_data(inssa)
elif num == '2':
    print('실시간 검색어 보기')
elif num == '3':
    print('실시간 뉴스속보 보기')
elif num == '4':
    print('.일간 노래순위 보기')
    inssa = get_data()
    for m in inssa:
        print(f"{m[0]}위 {m[1]} - {m[2]}")
elif num == '5':
    print('영화 예매순위 보기')