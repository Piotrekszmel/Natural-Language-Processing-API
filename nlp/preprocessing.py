from typing import List, Dict
import re


class Tokenizer:
    def __init__(self) -> None:
        self.tokens = []
        self.word2idx = {}

    def word_tokenize(self, sent: str) -> List:
        s = re.sub('([.,!?()#])', r' \1 ', sent)
        s = re.sub('\s{2,}', ' ', s)
        if len(self.tokens) == 0:
            self.tokens = re.split("\s+", s)[:-1]
            return self.tokens

    def create_word2idx(self) -> Dict:
        assert len(self.tokens) > 0, "First create tokens"
        self.word2idx = {v: k for (k, v) in enumerate(set(self.tokens))}
        return self.word2idx

    def fit_on_text(self) -> None:
        assert len(self.tokens) > 0, "First create tokens"
        print(self.tokens)
        self.create_word2idx()
        self.text = [self.word2idx[w] for w in self.tokens]
    
    def create_idx2word(self) -> Dict:
        assert len(self.word2idx) > 0, "First create word2idx"
        self.idx2word = {v: k for (k, v) in self.word2idx.items()}
        return self.idx2word
    
    def __repr__(self):
        return (f"tokens: {self.tokens}")
