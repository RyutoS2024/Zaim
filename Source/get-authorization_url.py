from requests_oauthlib import OAuth1Session

# コンシューマIDとコンシューマシークレットを設定
consumer_key = ''
consumer_secret = ''

# リクエストトークンとシークレット
request_token = ''
request_token_secret = ''

# 認証URL
authorization_base_url = 'https://auth.zaim.net/users/auth'

# OAuthセッションの再開（リクエストトークンとシークレットを使用）
oauth = OAuth1Session(consumer_key,
                      consumer_secret,
                      resource_owner_key=request_token,
                      resource_owner_secret=request_token_secret)

# 認証コードを受け取るURLを作成する
authorization_url = oauth.authorization_url(authorization_base_url)

print('URLをブラウザで実行する: ', authorization_url)