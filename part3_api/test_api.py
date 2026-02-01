import requests

api_url = "http://127.0.0.1:8000/api/assess-cv-risk"

def test_moderate_risk():
    moderate_example = {
        "blood_pressure": {"systolic": 138, "diastolic": 85},
        "fasting_glucose": 110,
        "bmi": 27.5,
        "age": 55
    }
    try:
        response = requests.post(api_url, json=moderate_example)
        if response.status_code != 200:
            raise RuntimeError(
                f"API error: {response.status_code} - {response.text}"    
            )
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


def test_low_risk():
    low_example = {"blood_pressure": {"systolic": 100, "diastolic": 70}, "fasting_glucose": 99, "bmi": 20, 
"age": 37}
    try:
        response = requests.post(api_url, json=low_example)
        if response.status_code != 200:
            raise RuntimeError(
                f"API error: {response.status_code} - {response.text}"    
            )
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
   
if __name__ == "__main__":
    test_moderate_risk()
    test_low_risk()
