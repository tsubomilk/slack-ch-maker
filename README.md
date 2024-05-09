# slackチャンネルを複数個同時に作る方法
大学授業のTeachingAssistantで、26個のチームチャンネルを一度に作成する機会があり、自動化するために作成。<br>
<br>
<img width="200" alt="スクリーンショット 2024-05-08 19 12 53" src="https://github.com/tsubomilk/slack-ch-maker/assets/78514031/b1d1c206-db33-4a98-9d37-6f509feb9bbe">

## 1.slack appをワークスペースにインストール
### ステップ1: Slack APIに登録する
Slackの開発者ポータルへのアクセス: Slack APIのウェブサイトにアクセスし、「Your Apps」に移動します。
新しいアプリを作成: 「Create New App」ボタンをクリックし、アプリに名前を付け、開発を行うSlackワークスペースを選択します。
### ステップ2: 機能と許可の設定
機能の追加: アプリの管理ページから、アプリに必要な機能（例えば、メッセージの送信、チャンネル管理など）を追加します。これには「Features」セクションで各種機能を設定します。
スコープの設定: 「OAuth & Permissions」ページで、アプリがユーザーやチャンネルのデータにアクセスするために必要なスコープ（許可）を追加します。
チャンネルを作成・メンバー追加するには groups:write,channels:manage,groups:write,channels:read,channels:writeまたはgroups:readとの権限が必要です。

### ステップ3: アプリのインストールと認証
アプリをワークスペースにインストール: 「OAuth & Permissions」ページで「Install App to Workspace」ボタンをクリックして、アプリをワークスペースにインストールします。
アクセストークンの取得: インストール後、ページ上でボットユーザーOAuthアクセストークン（通常 xoxb- で始まる）が生成されます。このトークンを使用してAPIリクエストを認証します。

## 2.コードにアクセストークン貼り付け

## 3.命名規則の指定
今回は、 '1-class-デザイン思考a-a'~ '1-class-デザイン思考a-z'を制作。



