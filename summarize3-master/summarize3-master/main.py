from OktTokenizer import OktTokenizer
from textrankr import TextRank
from TotalSql import TotalSql

def main():
  mytokenizer: OktTokenizer = OktTokenizer()
  textrank: TextRank = TextRank(mytokenizer)

  conts = TotalSql.findContent()
  for cont in conts:
    summarized: str = textrank.summarize(cont[1])
    print(summarized)
    TotalSql.insertSum(cont[0], summarized)

if __name__ == "__main__":
    main()