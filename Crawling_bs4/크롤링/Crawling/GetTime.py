# GetTime.py
import datetime 
from NewsExtract import NewsExtract
from NewsSql import NewsSql

class GetTime():
    # 시간 처리해서 가져오기
    @staticmethod
    def getTime(numdays) :                                                                  # 나오게할 날짜 갯수
        baseDate = datetime.date.today()                                                    # 오늘 날짜를 기준으로 잡아
        d_list = [baseDate - datetime.timedelta(days=x) for x in range(numdays)]            # 오늘로부터 인자로 받은 숫자 전의 날짜 가져오기
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list :                                                                # 날짜 수 만큼 반복돌리기
            temp = date.strftime("%Y%m%d")                                                  # 날짜 형태 문자열로 바꾸기
            date_list.append(temp)                                                          # 리스트에 추가
        return date_list                                                                    # 리턴

    # 2019년부터 가져오기
    @staticmethod
    def getTime_Past() :                                                                    # 과거 데이터 가져오기
        baseDate = datetime.date(2019, 1, 1)                                                # 기준일은 2019년 1월 1일
        d_day = datetime.date.today() - baseDate                                            # 오늘 날짜 - 기준일의 d-day 구하기
        d_day = int(str(d_day)[0:4])                                                        # d-day에서 날짜 부분만 가져오기
        d_list = [baseDate + datetime.timedelta(days=x) for x in range(d_day)]              # d-day 수 만큼 날짜 리스트 만들기
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 


    @staticmethod
    def compareTime(news):
        # 현재 기사의 시간
        nTime = news.time
        nTime_Sec = nTime[:10] + nTime[11:] + ":00"             # 기사 시간을 원하는 형태의 형식으로 만들기
        nTime_Sec = nTime_Sec.replace(".", "-")

        # DB에 저장된 마지막 시간
        try:
            lTime = NewsSql.findMaxTimeNews()
            lastTime = lTime.strftime("%Y-%m-%d %H:%M:%S")      # datetime.datetime 형식을 str로 변경
        except:
            lastTime = '1900-01-01 12:30:00'                    # 데이터베이스에 날짜가 없으면 1900-01-01 12:30:00으로 만들기
        finally:
            # 현재 기사 시간이 DB에 저장된 시간보다 이전인 경우 1, 아닐 경우 0 return
            if nTime_Sec < lastTime:
                return 1
            else:
                return 0