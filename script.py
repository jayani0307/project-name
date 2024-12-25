import requests

url = "https://raw.githubusercontent.com/jayani0307/project-name/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to fetch the script. Status code: {response.status_code}")
