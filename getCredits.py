import requests
import json

from config import headers

try:
    # APIリクエストを送信
    response = requests.get('https://api.pingdom.com/api/3.1/credits', headers=headers)
    response.raise_for_status()

    # レスポンスデータをJSON形式で取得
    credits_info = response.json()
    print(json.dumps(credits_info, indent=2))

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err} - {response.text}")
except Exception as err:
    print(f"An error occurred: {err}")
