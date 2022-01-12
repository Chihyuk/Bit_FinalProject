from OktTokenizer import OktTokenizer
from textrankr import TextRank
from TotalSql import TotalSql
import time
import threading

def main(a=2):
  mytokenizer: OktTokenizer = OktTokenizer()
  textrank: TextRank = TextRank(mytokenizer)

  if a == 1:
    conts = TotalSql.findContent()
    for cont in conts:
      summarized: str = textrank.summarize(cont[1])
      print(cont[0])
      TotalSql.insertSum(cont[0], summarized)

  elif a == 2:
    conts = TotalSql.findContent_front()
    exist = 0
    for cont in conts:
      summarized: str = textrank.summarize(cont[1])
      print(cont[0])
      exist = TotalSql.insertSum_front(cont[0], summarized, exist)
      if exist >= 5:
        break
    threading.Timer(180, main).start()

if __name__ == "__main__":
    main(2)