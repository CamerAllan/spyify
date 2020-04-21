from mitmproxy import ctx
from mitmproxy import http
import json
import csv
import os
import re
from datetime import datetime

user_activity = {}
friend_activity = {}


def log_activity(in_mem_storage):
    date_string = datetime.today().strftime("%Y-%m-%d")
    filepath = f"./out/{date_string}.csv"
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, "a") as f:
        writer = csv.writer(f)
        writer.writerows(in_mem_storage.items())
        in_mem_storage.clear()


def process_friend_activity(response_text):
    info = json.loads(response_text)
    print(f"New activity logged at timestamp: {info['timestamp']}")
    print(f" User: {info['user']['name']}")
    print(f" Track: {info['track']['name']} - {info['track']['artist']['name']}")

    friend_activity[f"{info['user']['uri']}-{info['timestamp']}"] = info
    log_activity(friend_activity)


def response(flow: http.HTTPFlow):

    presence_view_url = "https://spclient.wg.spotify.com/presence-view/"

    pretty_url = flow.request.pretty_url

    if presence_view_url in pretty_url:
        process_friend_activity(flow.response.text)
