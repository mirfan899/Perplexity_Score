import nltk
from nltk.lm import MLE
from nltk.lm import Vocabulary
import pickle

train_sentences = ['an apple', 'an orange', "an ant", "The quick brown fox jumps over the lazy dog."]
tokenized_text = [list(map(str.lower, nltk.tokenize.word_tokenize(sent))) for sent in train_sentences]

n = 1
train_data = [nltk.bigrams(t,  pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>") for t in tokenized_text]
words = [word for sent in tokenized_text for word in sent]
words.extend(["<s>", "</s>"])
padded_vocab = Vocabulary(words)
model = MLE(n)
model.fit(train_data, padded_vocab)
f = open("models/unigram_ppl_model.pkl", "wb")

pickle.dump({"model": model}, f)

