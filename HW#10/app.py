import tweepy
from flask import Flask, request, jsonify

app = Flask(__name__)


def OAuth():
    CONSUMER_API_KEY = 'LLOA3SnXqQRGI7zmAQ2rfbxg0'
    CONSUMER_API_SECRET_KEY = 'go2jL7IdEoapPQxN98VCHRcMxYecqGU6rt4z82Ebzoi32Hkm6O'
    USER_ACCESS_TOKEN = '858617944229720064-PAqEsTxCdPYSaUrWQBPEvNQtSApeFr5'
    USER_SECRET_TOKEN = 'l2grxMlfTmXMgpGA5eqH2MQMfwqeP3CQAJCFTJ9qFq4Fh'

    try:
        auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
        auth.set_access_token(USER_ACCESS_TOKEN, USER_SECRET_TOKEN)
        return auth
    except Exception as e:
        return None


@app.route("/post", methods=['POST'])
def post():
    try:
        import requests
        import json
        URL = 'https://prodapimalik.azure-api.net/post/manual/paths/invoke'
        data = {
            'message': request.json['message']
        }
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': 'f6b96abefc944e02bd65914c73f6cb61',
            'Ocp-Apim-Trace': 'true'
        }
        response = requests.post(URL, data=json.dumps(data), headers=headers)
    finally:
        return "OK"


@app.route('/twitter', methods=['POST'])
def twitter_update_status():
    import tweepy

    oauth = OAuth()
    api = tweepy.API(oauth)

    try:
        response = api.update_status(request.json['message'])
    except Exception as e:
        pass
    finally:
        return jsonify(
            {
                'response': 'OK'
            }
        )
