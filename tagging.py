import nltk
import nltk.tag
import nltk.tokenize

TRAIN_DATA = [
    [('do', 'ACTION_DO'), ('meeting', 'FOO')],
    [('add', 'ACTION_ADD'), ('meeting', 'DATE_TYPE')],
    ]

re_patterns = [('..:..', 'TIME')]
re_tagger = nltk.tag.RegexpTagger(re_patterns)

tagger = nltk.tag.TrigramTagger(train=TRAIN_DATA, backoff=re_tagger)

print tagger.tag(["add", "meeting", "at", "20:00"])
print tagger.tag(["do", "meeting"])
