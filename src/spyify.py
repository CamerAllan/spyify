from mitmproxy import ctx
from mitmproxy import http
import json
from datetime import datetime


def response(flow: http.HTTPFlow):

    presence_view_url = "https://spclient.wg.spotify.com/presence-view/"

    if presence_view_url in flow.request.pretty_url:
        activity_text = flow.response.text
        info = json.loads(flow.response.text)

        print(info)
        timestamp = datetime.fromtimestamp(info["timestamp"])

        print(f"New activity logged at timestamp: {timestamp}")
        print(f" User: {info['user']['name']}")
        print(f" Track: {info['track']['name']} - {info['track']['artist']['name']}")
