import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '{ "sentence": "the quick brown fox jumps over the lazy dog." }'

response = requests.post('http://127.0.0.1:8000/perplexity_score/', headers=headers, data=data)

print(response.text)
