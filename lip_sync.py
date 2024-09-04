import assemblyai as aai
import os
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, ColorClip

# AssemblyAI setup
aai.settings.api_key = "your API key"
transcriber = aai.Transcriber()

# Transcribe the audio file
transcript = transcriber.transcribe("./untitled.wav")

words = transcript.words

# Define viseme mapping
viseme_mapping = {
    'MBP': 'closed_lips.png',      # M, B, P
    'AI': 'open_wide.png',         # A, I
    'OU': 'rounded_mouth.png',     # O, U
    'FV': 'teeth_visible.png',     # F, V
    'EEXY': 'slightly_open.png',   # EE, I, Y
    'TH': 'tongue_between_teeth.png', # TH
    'SZDGNTK': 'stretched_wide.png',  # S, Z, D, G, N, T, K
    'R': 'slightly_rounded.png',   # R
    'CHJSH': 'pursed_lips.png'     # CH, J, SH
}

def get_viseme_for_word(word):
    # Strip punctuation from word
    word = word.strip(".,!?").upper()
    
    # Determine the viseme based on the first or last letter
    for letters, viseme in viseme_mapping.items():
        if word[0] in letters or word[-1] in letters:
            return viseme
    
    # Default to 'closed_lips.png' if no match found
    return 'closed_lips.png'

# Process words and map to viseme
def process_words_to_viseme(words):
    results = []

    for word_info in words:
        word = word_info.text.strip(".,!?")
        viseme = get_viseme_for_word(word)
        start_time = word_info.start
        end_time = word_info.end

        results.append({
            'word': word,
            'start_time': start_time,
            'end_time': end_time,
            'viseme': viseme
        })

    return results

# Create a sequence of PNG images based on timing
def create_lip_sync_video(processed_words, output_dir, audio_file, fps=24, resolution=(1920, 1080)):
    # Create a white background clip
    background = ColorClip(size=resolution, color=(255, 255, 255), duration=1)
    
    # Collect all images and their display times
    clips = []
    previous_end_time = 0

    for word_data in processed_words:
        viseme = word_data['viseme']
        start_time = word_data['start_time']
        end_time = word_data['end_time']
        duration = (end_time - start_time) / 1000  # Convert milliseconds to seconds

        # Handle the gap between words
        if start_time > previous_end_time:
            gap_duration = (start_time - previous_end_time) / 1000
            gap_clip = ImageClip(os.path.join(output_dir, 'closed_lips.png'), duration=gap_duration)
            gap_clip = gap_clip.resize(height=resolution[1]).set_position('center')
            clips.append(CompositeVideoClip([background, gap_clip], size=resolution).set_duration(gap_duration))

        # Path to the image
        image_path = os.path.join(output_dir, viseme)
        if os.path.exists(image_path):
            image_clip = ImageClip(image_path, duration=duration)
            image_clip = image_clip.resize(height=resolution[1]).set_position('center')
            clips.append(CompositeVideoClip([background, image_clip], size=resolution).set_duration(duration))
        
        previous_end_time = end_time
    
    # Concatenate all clips into one video
    video = concatenate_videoclips(clips, method="compose")
    
    # Add audio
    audio_clip = AudioFileClip(audio_file)
    video = video.set_audio(audio_clip)
    
    # Write the final video file with audio
    video_path = os.path.join(output_dir, 'lip_sync_video.mp4')
    video.write_videofile(video_path, fps=fps)

# Run the function and create the video
output_directory = '.'  # Change to your PNG directory if needed
audio_file_path = './untitled.wav'  # Path to your audio file
processed_words = process_words_to_viseme(words)
create_lip_sync_video(processed_words, output_directory, audio_file_path)
