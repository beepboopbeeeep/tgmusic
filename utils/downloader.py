import os
import yt_dlp
import requests
from bs4 import BeautifulSoup
from config import TEMP_PATH

def download_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{TEMP_PATH}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info).replace('.webm', '.mp3')

def download_instagram(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Get HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find video URL
    video_url = None
    meta_tag = soup.find('meta', property='og:video')
    if meta_tag:
        video_url = meta_tag['content']
    
    if not video_url:
        raise Exception("Couldn't find video URL")
    
    # Download video
    file_path = f"{TEMP_PATH}instagram_video.mp4"
    with requests.get(video_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    return file_path

def download_tiktok(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Get HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find video URL
    video_url = None
    script_tags = soup.find_all('script')
    for script in script_tags:
        if 'video_url' in script.text:
            start = script.text.find('"video_url":"') + len('"video_url":"')
            end = script.text.find('"', start)
            video_url = script.text[start:end].replace('\\u002F', '/')
            break
    
    if not video_url:
        raise Exception("Couldn't find video URL")
    
    # Download video
    file_path = f"{TEMP_PATH}tiktok_video.mp4"
    with requests.get(video_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    return file_path

def download_pinterest(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Get HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find video URL
    video_url = None
    script_tags = soup.find_all('script')
    for script in script_tags:
        if '"videoUrl":"' in script.text:
            start = script.text.find('"videoUrl":"') + len('"videoUrl":"')
            end = script.text.find('"', start)
            video_url = script.text[start:end]
            break
    
    if not video_url:
        raise Exception("Couldn't find video URL")
    
    # Download video
    file_path = f"{TEMP_PATH}pinterest_video.mp4"
    with requests.get(video_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    return file_path

def download_soundcloud(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{TEMP_PATH}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info).replace('.webm', '.mp3')

def download_media(url, platform):
    if platform == 'youtube':
        return download_youtube(url)
    elif platform == 'instagram':
        return download_instagram(url)
    elif platform == 'tiktok':
        return download_tiktok(url)
    elif platform == 'pinterest':
        return download_pinterest(url)
    elif platform == 'soundcloud':
        return download_soundcloud(url)
    else:
        raise Exception("Unsupported platform")