import requests
from requests_oauthlib import OAuth1
import json

# あなたのコンシューマキー、コンシューマシークレット、アクセストークン、アクセストークンシークレットを設定
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth1認証セッションの作成
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

# パラメータ
# 開始日時：2023-02-22
# 終了日時：2023-02-23
params = {
    'mapping': 1,
    'start_date': '2024-02-22',
    'end_date': '2024-02-23'
}


# GETリクエストの送信
response = requests.get('https://api.zaim.net/v2/home/money', auth=auth, params=params)

# レスポンスの確認
if response.status_code == 200:
    # レスポンスの内容をJSON形式で出力
    response_data = response.json()
    # JSONデータを整形して出力
    print(json.dumps(response_data, indent=4, sort_keys=True))
else:
    print(f'Error: {response.status_code}')
