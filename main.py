from youtube_transcript_api import YouTubeTranscriptApi

url = input("Введите ссылку на видео: ")
url = url.replace("youtube.com/watch?v=", "").replace("https://", "").replace("www.", "")

subtitles = YouTubeTranscriptApi.get_transcript(url, languages=['ru'])

with open(f"{url}.txt", "w" , encoding='utf-8') as file:
    for subtitle in subtitles:
        file.writelines(f"{subtitle['text']}")