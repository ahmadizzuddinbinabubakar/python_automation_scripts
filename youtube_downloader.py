from pytube import YouTube

#if CERTIFICATE_VERIFY_FAILED error: 
#1. pip install certifi
#2. sh <python path>/Install Certificates.command

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
s

link = input("Enter the YouTube video URL: ")
Download(link)