#!/bin/bash

# This script is used to generate a bearer token from the twitch API

# Set the client ID and secret

CLIENT_ID=""
CLIENT_SECRET=""
curl -X POST "https://id.twitch.tv/oauth2/token?client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&grant_type=client_credentials" >> secrets.py

