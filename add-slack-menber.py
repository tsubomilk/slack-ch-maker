import requests
import string

# トークンの設定
token = 'xoxb-slackappからアクセストークンをコピーしてくる'
headers = {'Authorization': f'Bearer {token}'}

# メンバーをチャンネルに追加する関数
def add_members_to_channel(channel_id, user_ids):
    url = 'https://slack.com/api/conversations.invite'
    data = {'channel': channel_id, 'users': ','.join(user_ids)}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200 and response.json()['ok']:
        print(f"Members successfully added to channel ID {channel_id}.")
    else:
        print(f"Failed to add members to channel {channel_id}: {response.json().get('error')}")

# チャンネルIDを取得する関数
def get_channel_id(channel_name):
    url = 'https://slack.com/api/conversations.list'
    params = {'types': 'public_channel', 'exclude_archived': 'true', 'limit': 1000}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200 and response.json()['ok']:
        channels = response.json()['channels']
        for channel in channels:
            if channel['name'] == channel_name:
                return channel['id']
    return None

# ユーザーIDリスト
user_ids = ['XXXXXXX', 'XXXXXXX', 'XXXXXXX']

# チャンネル名の生成とメンバーの追加
base_name = '1-class-デザイン思考a-'
for char in string.ascii_lowercase:
    channel_name = f"{base_name}{char}"
    channel_id = get_channel_id(channel_name)
    if channel_id:
        add_members_to_channel(channel_id, user_ids)
    else:
        print(f"Channel {channel_name} not found.")
