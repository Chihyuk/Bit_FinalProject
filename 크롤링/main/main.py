# -*- coding: utf-8 -*-
# main.py

from Function import Function
from FindNewsCat import FindNewsCat
import time
import threading

def main():
    print("==================메뉴==================")
    print("1. bs4 선택")
    print("2. selenium 선택")
    select1 = input("숫자를 입력해주세요 : ")
    if int(select1) == 1:
        print("Beautifulsoup를 선택하였습니다.")
        print("1. 언론사 업데이트")
        print("2. 과거 뉴스 넣기")
        print("3. 최신 뉴스 넣기")
        print("4. 카테고리 넣기")
        select2 = input("숫자를 입력해주세요 : ")
        if int(select2) == 1:
            print("언론사 업데이트 중")
            Function.press()
            print("언론사 업데이트가 끝났습니다.")
        elif int(select2) == 2:
            print("과거 뉴스 정보를 DB에 넣습니다.")
            Function.pastNews()
        elif int(select2) == 3:
            print("최신 뉴스 정보를 DB에 넣습니다.")
            #Function.presentNews()
        elif int(select2) == 4:
            print("카테고리 찾아 넣기")
            FindNewsCat.findNewsCat()
    elif int(select1) == 2:
        print("Selenium을 선택하였습니다.")


def today():
    
    print("sid1 = 100 에 해당하는 기사 가져오기")
    Function.presentNews0()

    print("sid1=100에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300)

    
    print("sid1 = 101 에 해당하는 기사 가져오기")
    Function.presentNews1()

    print("sid1=101에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300)

    
    print("sid1 = 102 에 해당하는 기사 가져오기")
    Function.presentNews2()

    print("sid1=102에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300)

    
    print("sid1 = 103 에 해당하는 기사 가져오기")
    Function.presentNews3()

    print("sid1=103에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300)

    
    print("sid1 = 104 에 해당하는 기사 가져오기")
    Function.presentNews4()

    print("sid1=104에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300)

    
    print("sid1 = 105 에 해당하는 기사 가져오기")
    Function.presentNews5()       

    print("sid1=104에 해당하는 기사를 다 넣었습니다.")
    print("잠들기 시작")
    time.sleep(300) 

    threading.Timer(300, today).start()

if __name__ == "__main__":
    #main()
    today()