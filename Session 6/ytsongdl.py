from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Natural Imagine Dragons', 'Youngblood 5 Seconds of Summer'])