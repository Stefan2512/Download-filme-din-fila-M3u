import os
import yt_dlp

def download_from_m3u(m3u_file, download_dir, username, password):
    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    with open(m3u_file, 'r') as file:
        lines = file.readlines()

    # Add authentication info to the URLs if not present
    urls = []
    for line in lines:
        line = line.strip()
        if line.startswith("http"):
            if "username=" not in line or "password=" not in line:
                # Append username and password to the URL
                line += f"&username={username}&password={password}"
            urls.append(line)

    # Download each URL
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                print(f"Downloading {url}...")
                ydl.download([url])
            except Exception as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    # Specify your M3U file, download directory, and authentication
    m3u_file = 'path/to/your/playlist.m3u'
    download_dir = 'path/to/download/directory'
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'
    
    download_from_m3u(m3u_file, download_dir, username, password)
