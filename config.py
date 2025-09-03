import os

# Railway Environment Variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
ACRCLOUD_ACCESS_KEY = os.environ.get("ACRCLOUD_ACCESS_KEY")
ACRCLOUD_ACCESS_SECRET = os.environ.get("ACRCLOUD_ACCESS_SECRET")
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN")
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
MUSIXMATCH_API_TOKEN = os.environ.get("MUSIXMATCH_API_TOKEN")

# File size limit (30MB)
MAX_FILE_SIZE = 30 * 1024 * 1024

# Download paths
DOWNLOAD_PATH = "downloads/"
TEMP_PATH = "temp/"

# Supported platforms
SUPPORTED_PLATFORMS = {
    'youtube': ['youtube.com', 'youtu.be'],
    'instagram': ['instagram.com', 'instagr.am'],
    'tiktok': ['tiktok.com'],
    'pinterest': ['pinterest.com', 'pin.it'],
    'soundcloud': ['soundcloud.com']
}

# Create directories if they don't exist
os.makedirs(DOWNLOAD_PATH, exist_ok=True)
os.makedirs(TEMP_PATH, exist_ok=True)