import requests
import string

# トークンの設定（セキュリティのため、通常は環境変数から読み込むことを推奨）
token = 'xoxb-slackappからアクセストークンをコピーしてくる'
headers = {'Authorization': f'Bearer {token}'}

# チャンネルを作成する関数
def create_channel(name):
    url = 'https://slack.com/api/conversations.create'
    data = {'name': name}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200 and response.json()['ok']:
        print(f"Channel {name} created successfully.")
    else:
        print(f"Failed to create channel {name}: {response.json().get('error')}")

# チャンネル名の生成とチャンネルの作成
base_name = '1-class-デザイン思考a'
for char in string.ascii_lowercase:
    channel_name = f"{base_name[:-1]}{char}"
    create_channel(channel_name)
