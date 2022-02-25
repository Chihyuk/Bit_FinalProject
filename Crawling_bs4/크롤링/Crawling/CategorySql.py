# CategorySql.py
# 뉴스 카테고리를 넣기 위한 sql문 모음집
from SqlCon import SqlCon

class CategorySql():
    @staticmethod
    def insertCat(c_id, c_name):        # 카테고리 아이디와 카테고리 이름을 인자로 받아 값 넣기
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_category (c_id, c_name) values({0}, '{1}')", c_id, c_name)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False

    @staticmethod
    def insertCatDet(cd_id, c_id, cd_name):     # 카테고리 디테일 아이디와 카테고리 아이디와 카테고리 디테일 이름을 인자로 받아 값 넣기
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_category_detail (cd_id, c_id, cd_name) values({0}, {1}, '{2}')", cd_id, c_id, cd_name)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False

