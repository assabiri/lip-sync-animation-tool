---

# Lip Sync Animation Tool

## Overview

This project is a Python-based tool designed to automate the lip-syncing process for animations. It uses AssemblyAI for speech transcription and MoviePy to generate synchronized lip movement videos based on audio input. The project was developed as a final project for CS50, inspired by the need for a more accessible and affordable lip sync solution than those offered by existing tools like Adobe Animate.

## Features

- **Automated Lip Syncing**: Transcribes audio files and matches the speech to appropriate mouth shapes (visemes).
- **Customizable Viseme Mapping**: Allows for easy customization of which mouth shapes correspond to different sounds.
- **Video Generation**: Creates a video sequence of images based on the timing of the speech, which is then synchronized with the original audio.
- **Affordable and Accessible**: Offers an open-source alternative to expensive animation tools.

## Motivation

The main reason for developing this project was the lack of effective and affordable lip-syncing tools for animation. While Adobe Animate provides some functionality, it’s not always reliable and can be quite expensive. This project aims to fill that gap by providing a simple, yet powerful, solution for animators.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/assabiri/lip-sync-animation-tool.git
```

2. Navigate to the project directory:

```bash
cd lip-sync-animation-tool
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Set up your AssemblyAI API key:

   - Sign up for a free account on [AssemblyAI](https://www.assemblyai.com/).
   - Get your API key from the dashboard.
   - Update the `aai.settings.api_key` in the code with your API key.

## Usage

1. Prepare your audio file (e.g., `untitled.wav`).

2. Prepare your viseme images (e.g., `closed_lips.png`, `open_wide.png`, etc.) and place them in the project directory.

3. Run the main script:

```bash
python lip_sync.py
```

4. The output video (`lip_sync_video.mp4`) will be generated in the same directory.

## Code Explanation

### Main Components

- **AssemblyAI Transcription**: Converts the input audio into text, helping determine the timing of words.
- **Viseme Mapping**: Maps phonetic sounds to corresponding mouth shape images.
- **Video Generation**: Creates a video by sequencing the viseme images according to the speech's timing and adds the original audio.

### Customization

- Modify the `viseme_mapping` dictionary to change how different sounds are visualized.
- Adjust the resolution or other video settings in the `create_lip_sync_video` function as needed.

## Future Improvements

- Add support for more phonemes and visemes.
- Implement a GUI for easier use.
- Optimize the video generation process for faster performance.

## License

This project is open-source and available under the MIT License.

---

## Acknowledgments

- **CS50**: For providing the foundation and inspiration to develop this project.
- **AssemblyAI**: For offering a robust transcription API that made this project possible.
- **MoviePy**: For the powerful video editing library used to create the final lip-sync videos.

---

## Contact

If you have any questions, suggestions, or want to contribute, feel free to contact me at [assabiriaymane@gmail.com].

---