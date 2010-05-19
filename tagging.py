import nltk
import nltk.tag
import nltk.tokenize

TRAIN_DATA = [
    [('fuck', 'ACTION'), ('meeting', 'FOO'), ('aaa', 'BAR')],
    [('add', 'ACTION'), ('meeting', 'aaa')],
    ]
#DATA = ["add", "23:00"]
#DATA = ["fuck", "meeting", "aaa"]
DATA = ["add", "meeting"]

re_patterns = [('..:..', 'TIME')]
re_tagger = nltk.tag.RegexpTagger(re_patterns)

tagger = nltk.tag.BigramTagger(train=TRAIN_DATA, backoff=re_tagger)

print tagger.tag(DATA)
