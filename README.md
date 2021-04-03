## Installation
Install `fastapi` for fast response
```shell
pip install fastapi
pip install uvicorn[standard]
pip install requests
```

## Training MLE model
Run the script `train_ppl_unigram` or `train_ppl_bigram.py`. These scripts will generate the MLE models for
perplexity. 

## Run Server
After training the model, run the api server by
```shell
uvicorn main:app --reload
```

## Testing
Now you can test the api with `api_test.py` script. Or run the `curl` command
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/perplexity_score/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentence": "an apple"
}'
```
