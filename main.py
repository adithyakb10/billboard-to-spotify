from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-public"
))

date = input("Enter the date(YYYY-MM-DD): ")

user_id = sp.me()['id']
playlist_name = f"Billboard Playlist {date}"
playlist_description = "Playlist created from Billboard song titles"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

track_ids = []

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("li ul li h3")
for title in titles:
    title = title.get_text(strip=True)
    result = sp.search(q=title, type='track', limit=1)
    tracks = result['tracks']['items']
    if tracks:
        track_ids.append(tracks[0]['id']) 
        print(f"Added {title} to the playlist")
    else:
        print(f"Couldn't add the track {title} to the playlist")

if track_ids:
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids)
    print(f"Added {len(track_ids)} songs to the playlist '{playlist_name}'.")
else:
    print("No tracks found to add to the playlist.")