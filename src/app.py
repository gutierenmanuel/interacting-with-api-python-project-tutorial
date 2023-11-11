import os
import pandas as pd
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("SECRET_ID")

artist_uri = 'spotify:artist:1a2b3c4d5e6f7g2ye2Wgw4gimLv2eAKyk1NB?si=T3WOLkgZSiispl0oV5TO2Q'



