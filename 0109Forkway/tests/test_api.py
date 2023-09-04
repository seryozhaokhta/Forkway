
import requests

BASE_URL = "http://localhost:8000"  # This would be the URL where the FastAPI app is running

def test_sample():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
