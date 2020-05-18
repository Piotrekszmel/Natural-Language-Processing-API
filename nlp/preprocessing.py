from typing import List
import re


class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.word2idx = {}

    def word_tokenize(self, sent: str) -> List:
        s = re.sub('([.,!?()#])', r' \1 ', sent)
        s = re.sub('\s{2,}', ' ', s)
        self.tokens = re.split("\s+", s)
        return self.tokens
    
    def create_word2idx(self):
        assert len(self.tokens) > 0, "First create tokens"
        self.word2idx = {k: v for (k, v) in enumerate(set(self.tokens))}
        return self.word2idx

    def fit_on_text(text: str):
        pass

t = Tokenizer()
tokens = t.word_tokenize("Hello man I am cool and cool and you")
word2idx = t.create_word2idx()
print(tokens)
print("\n")
print(word2idx) 