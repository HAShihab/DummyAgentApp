import requests

def test_chat_endpoint():
    url = "http://127.0.0.1:5000/chat"
    payload = {"message": "Hi"}
    
    try:
        response = requests.post(url, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Success!")
            print("AI Response:", response.json().get("reply"))
        else:
            print(f"Failed with status code: {response.status_code}")
            print("Error details:", response.text)
            
    except requests.exceptions.ConnectionError:
        print("Error: The Flask server is not running. Start it with 'python app.py' first.")

if __name__ == "__main__":
    test_chat_endpoint()