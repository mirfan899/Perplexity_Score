from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import nltk


def get_score(sentences=None):
    result = []
    test_sentences = [sentences]
    tokenized_text = [list(map(str.lower, nltk.tokenize.word_tokenize(sent))) for sent in test_sentences]
    test_data = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>") for t in
                 tokenized_text]
    for i, test in enumerate(test_data):
        result.append({"sentence": test_sentences[i], "score": model.perplexity(test)})

    return result


app = FastAPI()

pkl = open("models/bigram_ppl_model.pkl", "rb")
model = pickle.load(pkl)["model"]


class Perplexity(BaseModel):
    sentence: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/perplexity_score/")
async def score(sentences: Perplexity):
    return get_score(sentences.dict()['sentence'])
