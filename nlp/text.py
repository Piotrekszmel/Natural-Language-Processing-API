from typing import List
from collections import Counter
import re
import string


class Text:
    """
    Text manipulation class.
    
    Parameters:
    -----------
        text: string
            Text to be manipulated.
    """
    def __init__(self, text: str) -> None:
        self.body = re.split("\s+", text)
        self.text = text
        self.unique = set(self.body)
        self.count = self.count_occur()

    def find(self, word: str, n: int = None) -> List[int]:
        """
        Returns indexes (or first n indexes if n is specified) of a given word in text.

        Parameters:
        -----------
            word: string
                Word that will be searched in the text. 
            n: int
                Number of indexes that will be returned.

        """
        idxs = [index for index, w in enumerate(self.body) if w in [word,
                                                                    word+'.',
                                                                    word+',']]
        if n is not None:
            return idxs[:n]
        
        return idxs

    def concordance(self, word: str, size: int, ret: bool = 0) -> List[str]:
        """"
        Returns all occurrences of a given word with given amount of additionals words from left and right side.

        Parameters:
        -----------
            word: string
                Word that will be searched in the text.
            size: int
                Number of strings to be added to final string from left and right side of given word.

        """

        idxs = self.find(word)
        
        occurs = [self.body[index - size:index] + self.body[index:index + size + 1] for index in idxs]
        
        if ret:
            return occurs
        else:
            for occur in occurs:
                print(occur)

    def count_occur(self):
        cleaned_text = self.text.translate(str.maketrans('', '', string.punctuation))
        cleaned_text = re.split("\s+", cleaned_text)
        return Counter(cleaned_text)



t = Text("My name is Alex. Hope you have a good day. Alex, Alex. I hate you Alex")
print(t.count)
#t.concordance("Alex", 1, 1)
