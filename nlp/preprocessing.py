import re


class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.word2idx = {}

    def word_tokenize(self, sent: str):
        s = re.sub('([.,!?()#])', r' \1 ', sent)
        s = re.sub('\s{2,}', ' ', s)
        self.tokens = re.split("\s+", s)
        return self.tokens
    

t = Tokenizer()
tokens = t.word_tokenize("I am stupid. #Bro, come on")
print(tokens)
            