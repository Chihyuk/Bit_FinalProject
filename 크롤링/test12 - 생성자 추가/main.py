# main.py

from FindMainNews import FindMainNews
from FindNewsCat import FindNewsCat

url = 'https://news.naver.com/main/list.naver?mode=LS2D&' 

# url에 카테고리 포함시키기
cat_urls, cat_no = FindNewsCat.catInsert(url)

for cu in range(len(cat_urls)):
    # 완성된 뉴스 url로 만들기
    newsurls = FindMainNews.NewsInsert(cat_urls[cu], 1)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

    # 마지막 페이지까지 추출하기
    for no in range(len(newsurls)):
        try:
            news = FindMainNews.Extract(newsurls[no])

            print("제목 :", news.title)
            print("내용 :", news.content)
            print("날짜 :", news.time)
            print("원문 링크 :", news.link)
            print("사진 링크 :", news.pic_link)
            print("언론사 :", news.media)
            print("카테고리 :", news.cat)
            print("해당 세부 카테고리 : ", cat_no[cu][5:8])
            print("해당 카테고리 : ", cat_no[cu][14:17])

        except:
            continue


