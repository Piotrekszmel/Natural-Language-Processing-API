from typing import List
import re


class Text:
    def __init__(self, text: str) -> None:
        self.body = re.split("\s+", text)
        self.text = text

    def concordance(self, word: str, size: int, ret: bool = 0) -> List[str]:
        idxs = [index for index, w in enumerate(self.body) if w in [word,
                                                                    word+'.',
                                                                    word+',']]
        
        occurs = [self.body[index - size:index] + self.body[index:index + size + 1] for index in idxs]
        if ret:
            return occurs
        else:
            for occur in occurs:
                print(occur)


t = Text("My name is Alex. Hope you have a good day. Alex, Alex")
t.concordance("Alex", 3)


