from OktTokenizer import OktTokenizer
from textrankr import TextRank
from TotalSql import TotalSql

def main(a):
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
    for cont in conts:
      summarized: str = textrank.summarize(cont[1])
      print(cont[0])
      TotalSql.insertSum_front(cont[0], summarized)

if __name__ == "__main__":
    main(2)