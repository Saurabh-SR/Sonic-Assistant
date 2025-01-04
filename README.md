# Sonic Assistant

Sonic Assistant is an intelligent virtual assistant designed to simplify everyday tasks. 
It integrates speech recognition, text-to-speech synthesis and various functionalities like note-taking, weather updates, web browsing, and many more.
Its Super Scalable

---


## Features

1. **Voice Interaction:**
   - Responds to commands using natural language processing.
   - Uses text-to-speech for interaction.

2. **Web Browsing:**
   - Opens popular websites like YouTube, Google, Spotify and more.

3. **Music Playback:**
   - Plays predefined music stored locally.

4. **Time Announcements:**
   - Reads out the current time.

5. **Weather Updates:**
   - Fetches and reports current weather conditions for a specified city using the WeatherAPI.

6. **Application Launch:**
   - Opens installed applications like Tableau. We can add many more here

7. **Note-Taking:**
   - Allows users to create, read, and delete notes through voice commands.

8. **Search Functionality:**
   - Performs Google searches based on user queries.

9. **Exit Commands:**
   - Responds to shutdown commands to exit the assistant.

---

## Requirements

- Python 3.8+
- Internet connection for web-based services (e.g., weather, web browsing)
- Microphone for voice input
- Dependencies:
  - `speechrecognition`
  - `pypiwin32`
  - `requests`
  - `pyttsx3` (optional for speech synthesis)

---

## Installation
---

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/sonic-assistant.git
   cd sonic-assistant
   ```

Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up WeatherAPI:**
   -Sign up at WeatherAPI to get your API key.
   -Replace the placeholder in the weather_api variable with your API key.
   -Run the Assistant:
   ```bash   
   python main.py
   ```

