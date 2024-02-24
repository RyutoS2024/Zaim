from requests_oauthlib import OAuth1Session

# コンシューマIDとコンシューマシークレット
consumer_key = ''
consumer_secret = ''

# リクエストトークンとそのシークレット
request_token = ''
request_token_secret = ''

# 承認確認コード（verifier）
verifier = ''

# アクセストークン取得のURL
access_token_url = 'https://api.zaim.net/v2/auth/access'

# OAuthセッションの再開
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=request_token,
                      resource_owner_secret=request_token_secret,
                      verifier=verifier)

# アクセストークンを取得
access_token_response = oauth.fetch_access_token(access_token_url)

access_token = access_token_response.get('oauth_token')
access_token_secret = access_token_response.get('oauth_token_secret')

print("アクセストークン:")
print(f"oauth_token        = {access_token}")
print(f"oauth_token_secret = {access_token_secret}")
