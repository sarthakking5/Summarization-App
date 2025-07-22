from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

video_id = 'X7Zd4VyUgL0'
ytt_api=YouTubeTranscriptApi()
try:
    transcript = ytt_api.fetch(video_id=video_id)
    print(transcript)
except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("No transcript found for this video.")
except VideoUnavailable:
    print("The video is unavailable.")
except Exception as e:
    print(f"Unexpected error: {e}")