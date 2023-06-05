import sqlite3

# 데이터 넣기 함수
def save_data(inssa):
    # sqlite db 파일 생성 및 연결
    con = sqlite3.connect('database.db')
    # sql 문장을 실행시키기 위해 준비
    cursor = con.cursor()
    sql = '''
    INSERT INTO geni (title, artist)
    VALUES (?, ?)
    '''
    cursor.executemany(sql, inssa) # sql 을 실행
    con.commit() # 적용
    con.close()  # db닫기

# 데이터 보기 함수
def get_data():
    # sqlite db 파일 생성 및 연결
    con = sqlite3.connect('database.db')
    # sql 문장을 실행시키기 위해 준비
    cursor = con.cursor() 

    sql = '''
    SELECT * FROM geni
    '''
    cursor.execute(sql) # sql 을 실행
    # 하나의 데이터를 보기
    # data = cursor.fetchone()
    # print(data)

    # 전체 데이터 보기
    all_data = cursor.fetchall()
    # print(all_data)
    con.close()  # db닫기
    return all_data

def create_tb():
    con = sqlite3.connect('database.db')
    print(type(con))
    cursor = con.cursor() # sql 문장을 실행시키기 위해 준비
    sql = '''
    CREATE TABLE "geni" (
        "rank"    INTEGER NOT NULL,
        "title"  TEXT NOT NULL,
        "artist"  TEXT NOT NULL,
        PRIMARY KEY("rank" AUTOINCREMENT)
    )
    '''
    cursor.execute(sql) # sql 을 실행
    con.commit() # 적용
    con.close()  # db닫기

def drop_tb():
    con = sqlite3.connect('database.db')
    cursor = con.cursor() # sql 문장을 실행시키기 위해 준비
    sql = '''
        DROP TABLE geni
    '''
    cursor.execute(sql) # sql 을 실행
    con.commit() # 적용
    con.close()  # db닫기