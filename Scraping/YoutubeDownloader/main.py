import youtube_downloader
# Télécharger plusieurs vidéos 
'''
urls = ("https://www.youtube.com/watch?v=WlTlUseVt7E&list=RD4V90AmXnguw&index=2&ab_channel=MichaelJackson-Topic",
"https://www.youtube.com/watch?v=n3qQtSRmHxo&list=RD4V90AmXnguw&index=5&ab_channel=MichaelJackson-Topic")


for url in urls:
    youtube_downloader.download_video(url)
'''
# Télécharger une seule vidéo
url = "https://www.youtube.com/watch?v=WlTlUseVt7E&list=RD4V90AmXnguw&index=2&ab_channel=MichaelJackson-Topic"

youtube_downloader.download_video(url)







