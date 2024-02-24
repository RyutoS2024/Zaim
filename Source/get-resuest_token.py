from requests_oauthlib import OAuth1Session

# コンシューマIDとコンシューマシークレットを設定
consumer_key = ''
consumer_secret = ''

# リダイレクトURL
redirect_url = 'http://localhost:8080/oauth2/callback' 

# OAuthセッションを開始（ここでoauth_callbackを指定）
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri=redirect_url)

# リクエストトークン取得のURL
request_token_url = 'https://api.zaim.net/v2/auth/request'

try:
    # リクエストトークンを取得
    fetch_response = oauth.fetch_request_token(request_token_url)
    request_token = fetch_response.get('oauth_token')
    request_token_secret = fetch_response.get('oauth_token_secret')

    print("リクエストトークン：")
    print(f"oauth_token        = {request_token}")
    print(f"oauth_token_secret = {request_token_secret}")
except ValueError as e:
    # エラーメッセージを表示
    print(f"Error: {e}")
