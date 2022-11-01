# Projet "Yourube Downloade"

# pytube
# un stream est un flux
from ast import While
from pytube import YouTube
BASE_YOUTUBE_URL = "https://www.youtube.com"

# vérifier que l'url commence bien par https://www.youtube.com
# si ce n'est pas le cas 
# - afficher une erreur 
# - reposer la question


def get_video_url_from_user():
    while True:
        url = input("Url de la vidéo YouTube à télécharger : ")
        #if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
        if url.lower().startswith(BASE_YOUTUBE_URL):
            break
        print("ERREUR : Vous devez rentrer une URL YouTube")
    return url

# 1 - 144p
# 2 - 360p
# 3 - 720p
# Choisissez la résolution
# stream.resolution
# stream.itag

def get_video_stream_itag_from_user():
    print(" ")
    print("CHOIX DES RESOLUTIONS")
    streams = youtube_video.streams.filter(progressive=True, file_extension="mp4")
    index = 1
    for stream in streams:
        print(str(index) + "-" ,stream.resolution)
        index += 1
    while True:
        res_num = input("Choisissez la résolution : ")
        if res_num == "":
            print("ERREUR : Vous devez rentrer un nombre")
        else:
            try:
                res_num_int = int(res_num)
            except:
                print("ERREUR : Vous devez rentrer un nombre")
            else:
                if not 1<= res_num_int <= len(streams):
                    print("ERREUR : Vous devez rentrer un nombre entre 1 et " + str(len(streams)))
                else:
                    break
    itag = streams[res_num_int-1].itag
    return itag

# Afficher le pourcentage de téléchargement
def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print("Progression du téléchargement : " + str(int(percent)) + "%")

url = "https://www.youtube.com/watch?v=6p-lDYPR2P8&list=RDMM&start_radio=1&rv=h_D3VFfhvs4&ab_channel=Madonna"
#url = get_video_url_from_user()
youtube_video = YouTube(url)
streams = youtube_video.streams.filter(progressive=False, file_extension="mp4", type="video").order_by("resolution").desc()
video_stream = streams[0]
streams = youtube_video.streams.filter(progressive=False, file_extension="mp4", type="audio").order_by("abr").desc()
audio_stream = streams[0]
#print("STREAMS : ")
#for stream in streams:
#    print(stream)
print("Vidéo stream : ", video_stream)
print("Audio stream : ", audio_stream)

youtube_video.register_on_progress_callback(on_download_progress)

print("Titre  : " + youtube_video.title)
print("NB VUES : " + str(youtube_video.views))


#itag = get_video_stream_itag_from_user()

#stream = youtube_video.streams.get_by_itag(137)
#stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement vidéo...")
video_stream.download("vidéo")
print("OK")
print("Téléchargement audio...")
audio_stream.download("audio")
#stream.download()
print("OK")