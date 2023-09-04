
import requests

BASE_URL = "http://localhost:8000"  # This would be the URL where the FastAPI app is running

def generate_data():
    # Placeholder for generating users
    for _ in range(500):
        user_data = {
            "name": "Sample User",
            "phone": "1234567890",
            # ... other fields ...
        }
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        # Check if user creation was successful and handle any errors

    # Similar loops can be added for generating orders and visits

if __name__ == "__main__":
    generate_data()
