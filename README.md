# Twitch-chatbot
A chatbot for my twitch channel

Everything is build from the [twitchio](https://twitchio.dev/en/stable/quickstart.html) module.

## Running it

Setup your secrets.py as mentioned below, install your requirements and run it.
```bash
pip3 install -r requirements.txt
python3 main.py
```


## Secrets
Create a file called 'secrets.py' and add this:

```python
super_secret_password = "" # this is the token you get from the URL down below
less_hidden_token = "" # this is the bearer token, your can use the bearer script located in extra_tools
streamer = "" # The streamer/channel your want to start your bot in, should work in multiple 'user1, user2, user3' etc.
client_id = ""
client_secret = ""
```

Visit [this](https://twitchtokengenerator.com/) site (Token Generator) and select the Bot Chat Token. After selecting this you can copy your Access Token into the field in your `secrets.py` file.

