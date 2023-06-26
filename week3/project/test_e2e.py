import requests

FILE="/workspace/corise-mlops/week3/project/data/requests.json"
# URL="http://0.0.0.0/predict" # docker
URL="http://127.0.0.1:8000/predict"

def test_requests():
    file = open(FILE, "r")
    for line in file:
        response = requests.post(URL, data = line, headers = {"accept": "application/json", "Content-Type": "application/json"})
        assert response.status_code == 200
