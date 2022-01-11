# NewsCatSql.py

from SqlCon import SqlCon

class TotalSql():
    # 언론사 전체 가져오기
    @staticmethod
    def findContent():
        cursor = SqlCon.Cursor()
        query = str.format("select n_id, n_content from N_content")
        try: 
            cursor.execute(query)
            row = cursor.fetchall()
            SqlCon.Commit()
        except:
            return None
        else:
            #return row
            return row

    def insertSum(nid, nsc):
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, nsc)
        try: 
            cursor.execute(query)
            row = cursor.fetchall()     # 검색 결과 중에 하나의 Row를 fetch하시오.
            #row = cursor.fetchone()
            SqlCon.Commit()
        except:
            return None
        else:
            return True
