import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ag':2, 'au':9, 'cd':6, 'cu':23,'fe':3,'mn':3,'ni':2,'pb':3})

print(r.json())