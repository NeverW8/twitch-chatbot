# Twitch-chatbot
A chatbot for my twitch channel

Everything is build from the [twitchio](https://twitchio.dev/en/stable/quickstart.html) module.

## Running it

```bash
pip3 install -r requirements.txt
python3 main.py
```


## Secrets
Create a file called 'secrets.py' and add this:

```python
super_secret_password='your_access_token_here'
```

Visit [this](https://twitchtokengenerator.com/) site (Token Generator) and select the Bot Chat Token. After selecting this you can copy your Access Token into the field in your `secrets.py` file.

