import requests
import json
import secrets

channel_name = secrets.streamer
url = "https://api.twitch.tv/helix/streams?user_login=" + channel_name
bearer = secrets.super_secret_password
client_id = secrets.client_id


def get_stream():
    response = requests.get(url,
                            headers={"Authorization": "Bearer " + bearer, "Client-Id": client_id}).text
    data = json.loads(response)

    if data["data"] == []:
        return False
    else:
        return data["data"][0]


def get_stream_start_time():
    data = get_stream()
    print(data["started_at"])


get_stream()
get_stream_start_time()
