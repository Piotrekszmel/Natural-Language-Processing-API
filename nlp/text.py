from typing import List
import re


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


t = Text("My name is Alex. Hope you have a good day. Alex, Alex")
t.concordance("Alex", 2)

