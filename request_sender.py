import requests
import time
from datetime import datetime


def send_request(url):
    """Send a GET request to the specified URL and log the response."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Sending request to {url}...")
        
        response = requests.get(url)
        
        print(f"[{timestamp}] Status Code: {response.status_code}")
        print(f"[{timestamp}] Response Length: {len(response.text)} characters")
        print("-" * 80)
        
        return response
    except requests.exceptions.RequestException as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Error occurred: {e}")
        print("-" * 80)
        return None


def main():
    url = "https://arbit-backend-1.onrender.com/transformer-thermal-inspection/transformer-management/view-all"
    interval_seconds = 5 * 60  # 5 minutes in seconds
    
    print("Starting request sender...")
    print(f"URL: {url}")
    print(f"Interval: 5 minutes ({interval_seconds} seconds)")
    print("Press Ctrl+C to stop")
    print("=" * 80)
    
    try:
        while True:
            send_request(url)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nStopping request sender...")
        print("Goodbye!")


if __name__ == "__main__":
    main()
