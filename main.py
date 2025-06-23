import os
import requests
from gtts import gTTS
from moviepy.editor import *

def get_trending_topics():
    # Simulated trending topics (replace this with actual scraping if needed)
    return [
        "AI is revolutionizing healthcare",
        "Apple's new M4 chip benchmarks leaked",
        "Google launches Gemini 2 for developers"
    ]

def create_video(text, filename):
    # Generate voice
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")

    # Create text clip
    txt_clip = TextClip(text, fontsize=40, color='white', bg_color='black', size=(720, 1280))
    txt_clip = txt_clip.set_duration(10).set_position('center')

    # Add voice to video
    audio = AudioFileClip("voice.mp3")
    txt_clip = txt_clip.set_audio(audio)

    # Export video
    output_path = os.path.join("output", filename)
    txt_clip.write_videofile(output_path, fps=24)

def main():
    os.makedirs("output", exist_ok=True)
    topics = get_trending_topics()
    for i, topic in enumerate(topics):
        filename = f"video_{i+1}.mp4"
        print(f"Generating: {filename}")
        create_video(topic, filename)

if __name__ == "__main__":
    main()
