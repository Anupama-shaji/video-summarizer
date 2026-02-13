import yt_dlp

def extract_audio(url):
    output_path = "temp/audio.mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp/audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path
