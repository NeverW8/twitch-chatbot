import requests
import json
import secrets

channel_name = secrets.streamer
url = "https://api.twitch.tv/helix/streams?user_login=" + channel_name
bearer = secrets.less_hidden_token
client_id = secrets.client_id


def get_stream():
    response = requests.get(
        url, headers={"Authorization": "Bearer " + bearer, "Client-Id": client_id}
    ).text
    data = json.loads(response)["data"]

    if data == []:
        return False
    else:
        return True


def get_stream_start_time():
    if get_stream():
        response = requests.get(
            url, headers={"Authorization": "Bearer " + bearer, "Client-Id": client_id}
        ).text
        data = json.loads(response)["data"][0]
        return data["started_at"]
