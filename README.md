# Pingdom Monitoring Automation

このプロジェクトは、Pingdom APIを使用して自動的に複数のサーバを監視に追加するためのPythonスクリプトです。CSVファイルからサーバのリストを読み込み、PingdomにHTTPチェックとしてそれらのサーバを追加します。

## 前提条件

- Python 3.x
- `requests` ライブラリ（`pip install requests`でインストール可能）

## 設定

1. **APIキーの設定**:
   `config.py`ファイルを開き、`YOUR_API_KEY`を実際のPingdom APIキーに置き換えます。

2. **API公式Document
    使用しているAPIはchecks APIのpostです。parameterについては[公式Document](https://docs.pingdom.com/api/?_ga=2.230003480.509660209.1590495493-1793431897.1589990976#tag/Checks/paths/~1checks/post)を確認してください。


3. **サーバリストの準備**:
   `servers.csv`に監視したいサーバのリストを追加します。各行は次の形式に従う必要があります:

```csv
name,host,resolution,type,url,shouldnotcontain,encryption
test1,example.com,5,http,/,Error,True
test2,example.com,5,http,/,Error,True
```
|項目|説明|型
|---|---|---
|<span style="color: red;">*</span>name|名前|文字列型
|<span style="color: red;">*</span>host|ホスト名|文字列型
|resolution|チェック頻度|整数型 分単位
|<span style="color: red;">*</span>type|チェックするタイプ|"http" "httpcustom" "tcp" "ping" "dns" "udp" "smtp" "pop3" "imap"
|url|ターゲットのパス|文字列型
|shouldnotcontain|ターゲットサイト内に含まれない文字列|文字列型
|encryption|接続暗号化 default Bool型

<span style="color: red;">*</span>はrequired

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します:

```bash
python addUptimeCheck.py
```

このコマンドは、`servers.csv`にリストされた各サーバに対してPingdomでHTTPチェックを作成します。

## 注意事項

- APIキーは機密情報です。`config.py`を公開リポジトリにプッシュしないようにしてください。
- Pingdom APIの利用制限に注意してください。大量のリクエストを短時間で送信すると、制限を超える可能性があります。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
