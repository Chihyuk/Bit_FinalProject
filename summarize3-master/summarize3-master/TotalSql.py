# NewsCatSql.py

from SqlCon import SqlCon

class TotalSql():
    # 기사 내용 전체 가져오기
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
            return row

    # 기사 전체 내용 insert
    @staticmethod
    def insertSum(nid, nsc):
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, nsc)
        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return None
        else:
            return True

    # 기사 내용 앞에서 가져오기
    @staticmethod
    def findContent_front():
        cursor = SqlCon.Cursor()
        query = str.format("select n_id, n_content from N_content order by n_id desc")
        try: 
            cursor.execute(query)
            row = cursor.fetchall()
            SqlCon.Commit()
        except:
            return None
        else:
            return row

    # 앞에서 가져온 기사 넣기
    @staticmethod
    def insertSum_front(nid, nsc):
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, nsc)
        exist = 0
        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            exist += 1
            if exist >= 5:
                return None
            return None
        else:
            return True