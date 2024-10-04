# AudioRecognitionWithShazam

## Description
AudioRecognitionWithShazam is a Python application that allows users to record audio from their selected input device and identify songs using the Shazam API. The application captures audio for a specified duration and then processes the recording to recognize the song title, artist, album, and provides a link to the Shazam page.

## Features
- List available audio input devices.
- Select an audio input device for recording.
- Record audio for a specified duration.
- Recognize songs using the Shazam API.
- Display song details including title, artist, album, and Shazam link.

## Requirements
- Python 3.7 or higher
- `pyaudio`
- `wave`
- `shazamio`
- `asyncio`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/felipeczpaz/AudioRecognitionWithShazam.git
   cd AudioRecognitionWithShazam
   ```
2. Install the required packages:
   ```bash
   pip install pyaudio shazamio
   ```
   
## Usage
1. Run the application: 
   ```bash
   python main.py
   ```
2. Follow the prompts to select an audio input device and start recording.
3. After recording, the application will process the audio and display the recognized song details.

## Example
   ```bash
   Device 0: Microphone (Realtek High Definition Audio), Channels: 2
   Select an input device by index: 0
   Recording audio for 10 seconds...
   Recording stopped after specified duration.
   Title: Shape of You
   Artist: Ed Sheeran
   Album: ÷ (Divide)
   Shazam Link: https://www.shazam.com/track/123456789
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
