import requests

url = "https://google.com"

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("Website is UP")
    else:
        print("Website responded, but not OK")
except:
    print("Website is DOWN or unreachable")
