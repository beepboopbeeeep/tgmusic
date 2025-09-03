import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# Initialize Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

async def search_music(query):
    try:
        results = sp.search(q=query, type='track', limit=5)
        tracks = []
        
        for item in results['tracks']['items']:
            tracks.append({
                'name': item['name'],
                'artist': item['artists'][0]['name'],
                'id': item['id']
            })
        
        return tracks
    except Exception as e:
        print(f"Spotify search error: {e}")
        return []