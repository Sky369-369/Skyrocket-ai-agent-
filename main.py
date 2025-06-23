import os
from gtts import gTTS
from moviepy.editor import ColorClip, AudioFileClip

# Simulated trending topics
def get_trending_topics():
    return [
        "AI is revolutionizing healthcare with real-time diagnosis.",
        "Apple's new M4 chip benchmarks leaked and it’s breaking records.",
        "Google launches Gemini 2 – a game-changer for developers."
    ]

# Generate a simple video with background + voice
def create_video(text, filename):
    print(f"Generating video: {filename}")

    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")

    # Load voice audio
    audio = AudioFileClip("voice.mp3")

    # Create solid background video
    clip = ColorClip(size=(720, 1280), color=(0, 0, 0), duration=audio.duration)
    clip = clip.set_audio(audio)

    # Save final video
    output_path = os.path.join("output", filename)
    clip.write_videofile(output_path, fps=24)

# Main runner
def main():
    os.makedirs("output", exist_ok=True)
    topics = get_trending_topics()

    for i, topic in enumerate(topics):
        filename = f"video_{i+1}.mp4"
        create_video(topic, filename)

if __name__ == "__main__":
    main()
