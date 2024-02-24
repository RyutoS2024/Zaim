from requests_oauthlib import OAuth1Session
import json

# アクセストークンとそのシークレット
access_token = ''
access_token_secret = ''

# コンシューマIDとコンシューマシークレット
consumer_key = ''
consumer_secret = ''

# OAuthセッションの作成
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

# ユーザー情報を取得するエンドポイント
url = 'https://api.zaim.net/v2/home/user/verify'

# リクエストの送信
response = oauth.get(url)

# HTTPレスポンスのボディをJSON形式で解析する
response_data = response.json()

# JSONデータを整形して出力
print(json.dumps(response_data, indent=4, sort_keys=True))