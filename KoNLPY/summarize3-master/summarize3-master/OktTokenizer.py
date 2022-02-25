#-*-coding:utf-8-*-
from typing import List
from konlpy.tag import Okt


class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens








