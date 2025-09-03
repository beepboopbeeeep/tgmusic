from lyricsgenius import Genius
from lyrics_extractor import SongLyrics
from config import GENIUS_API_TOKEN, MUSIXMATCH_API_TOKEN

# Initialize Genius
genius = Genius(GENIUS_API_TOKEN)
genius.verbose = False
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

# Initialize Musixmatch
lyrics_extractor = SongLyrics(GENIUS_API_TOKEN, MUSIXMATCH_API_TOKEN)

def get_lyrics(track_name, artist_name):
    lyrics = None
    
    # Try Genius first
    try:
        song = genius.search_song(track_name, artist_name)
        if song and song.lyrics:
            lyrics = song.lyrics
    except Exception as e:
        print(f"Genius error: {e}")
    
    # Fallback to Musixmatch
    if not lyrics:
        try:
            result = lyrics_extractor.get_lyrics(f"{track_name} {artist_name}")
            if result and result.get('lyrics'):
                lyrics = result['lyrics']
        except Exception as e:
            print(f"Musixmatch error: {e}")
    
    return lyrics or "متن آهنگ یافت نشد"