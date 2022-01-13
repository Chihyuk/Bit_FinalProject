# Function.py

from FindMainNews import FindMainNews
from FindNewsCat import FindNewsCat
from FindPress import FindPress
from PressSql import PressSql
from NewsSql import NewsSql
from NewsExtract import NewsExtract
import re

class Function():

    # url을 전역변수로 선언
    global url
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&' 

    @staticmethod
    def press():
        # 언론사 테이블 넣기
        press = FindPress.findPress()
        PressSql.insertPress(press)

    @staticmethod
    def pastNews():
        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsert(url)
        sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        # 카테고리 수 만큼 for문 돌리기
        for cu in range(len(cat_urls)):
            sid1 = sid1_com.search(cat_no[cu]).group(2)
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPastNewsUrl(cat_urls[cu], sid1, sid2)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews():
        countdays = int(input("며칠 전까지 가져올까요? "))

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsert(url)
        sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid1 = sid1_com.search(cat_no[cu]).group(2)
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews0():
        countdays = 1
        sid1 = 100

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews1():
        countdays = 1
        sid1 = 101

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정


    @staticmethod
    def presentNews2():
        countdays = 1
        sid1 = 102

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews3():
        countdays = 1
        sid1 = 103

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews4():
        countdays = 1
        sid1 = 104

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    @staticmethod
    def presentNews5():
        countdays = 1
        sid1 = 105

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsertbySID1(url, sid1)
        #sid1_com = re.compile('(sid1=)([0-9]*)')
        sid2_com = re.compile('(sid2=)([0-9]*)')

        for cu in range(len(cat_urls)):
            sid2 = sid2_com.search(cat_no[cu]).group(2)
            print("==================================================================================================")
            print("현재 sid1은 ", sid1)
            print("현재 sid2는 ", sid2)

            # 완성된 뉴스 DB로 넣기
            FindMainNews.findAndInsertPresentNewsUrl(cat_urls[cu], sid1, sid2, countdays)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정