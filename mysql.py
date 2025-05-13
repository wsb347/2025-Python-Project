import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

db_pw = os.getenv("DB_PASSWORD")
db_user = os.getenv("MYSQL_USER")
db_name = os.getenv("DB_NANE")

# 1. MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',
    user=db_user,
    password=db_pw,
    database=db_name,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def execute_query(connection, query, params=None, fetch=False):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            else:
                connection.commit()
                return None
    except Exception as e:
        print(f"쿼리 실행 중 오류 발생: {e}")
        return None
